import numpy as np
import math
from scipy.spatial import procrustes
# ==============================================================================
# Modules
# ==============================================================================
# Built-ins
import os, sys, time, warnings
from collections import OrderedDict
# PyData
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean 

# Scikits
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
# from skbio.stats.ordination import pcoa, pcoa_biplot
# from skbio import DistanceMatrix
# from adjustText import adjust_text

# from ..io import write_object
# from ..utils import is_query_class, to_precision, dict_filter, is_symmetrical, is_nonstring_iterable, assert_acceptable_arguments
# from ..symmetry import Symmetric
# from ..visuals import plot_scatter

from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt

from collections import Counter
import pandas as pd
from collections import defaultdict
import pandas as pd




class Procrustes(object):
    """
    Python adaptation of https://rdrr.io/rforge/vegan/src/R/procrustes.R
    
    Differences: 
    * Symmetric defaults to True instead of False
    """
    def __init__(
        self,
        X,
        Y,
        name=None,
        n_components=2,
        scale=True,
        symmetric=True,
        ):
        
        def _ctrace(MAT):
            # https://rdrr.io/rforge/vegan/src/R/procrustes.R
            return np.sum(MAT.ravel()**2)
        
        # Initialize
        self.name = name
        self.scale = scale
        self.symmetric = symmetric
        self.n_components = n_components
        
        # Convert ordination objects into pd.DataFrames
        if hasattr(X, "projection_"):
            X = X.projection_
        if hasattr(Y, "projection_"):
            Y = Y.projection_

        # Assertions
        assert set(X.index) == set(Y.index), "X.index must have the same keys as Y.index"
        assert X.shape[1] >= n_components, "X.shape[1] = {} which is less than {}".format(X.shape[1], n_components)
        assert Y.shape[1] >= n_components, "Y.shape[1] = {} which is less than {}".format(Y.shape[1], n_components)
        
        # Reorder Y
        index = X.index
        Y = Y.loc[index]
        
        # Dimensions
        X = X.iloc[:,:n_components]
        Y = Y.iloc[:,:n_components]
        
        # Labels
        X_columns = X.columns
        Y_columns = Y.columns
        
        # Pandas -> NumPy
        X = X.values
        Y = Y.values
        
        # Center data
        # R Code: https://github.com/vegandevs/vegan/blob/83fd020085d6f294ea48496f91564600795c049c/R/procrustes.R
        #         if (symmetric) {
        #             X <- scale(X, scale = FALSE)
        #             Y <- scale(Y, scale = FALSE)
        #             X <- X/sqrt(ctrace(X))
        #             Y <- Y/sqrt(ctrace(Y))
        #         }
        #         xmean <- apply(X, 2, mean)
        #         ymean <- apply(Y, 2, mean)
        #         if (!symmetric) {
        #             X <- scale(X, scale = FALSE)
        #             Y <- scale(Y, scale = FALSE)
        #         }
        X_ = X.copy()
        Y_ = Y.copy()
        if symmetric:
            X_ = X_ - X_.mean(axis=0)
            Y_ = Y_ - Y_.mean(axis=0)
            X_ = X_/np.sqrt(_ctrace(X_))
            Y_ = Y_/np.sqrt(_ctrace(Y_))
            
        X_mean = X_.mean(axis=0)
        Y_mean = Y_.mean(axis=0)
        if not symmetric:
            X_ = X_ - X_mean
            Y_ = Y_ - Y_mean

        
        # Rotation
        XY = np.dot(X_.T, Y_) # crossprod(X,Y)
        U,s,Vh = np.linalg.svd(XY)
        V = Vh.T
        A = np.dot(V, U.T)
        
        c = 1
        if scale:
            c = np.sum(s)/_ctrace(Y_)
        Y_rotation = c * np.dot(Y_, A)
        
        self.n_ = X_.shape[0]
        self.X_ = pd.DataFrame(X_, index=index, columns=X_columns)
        self.X_mean_ = X_mean
        self.Y_ = pd.DataFrame(Y_, index=index, columns=Y_columns)
        self.Y_mean_ = Y_mean
        self.Y_rotation_ = pd.DataFrame(
            data = Y_rotation, 
            index=index, 
            columns=Y_columns,
        )
        self.labels_ = index
        self.svd_ = {"U":U, "s":s, "Vh":Vh }
        self.rotation_ = A
        self.scaling_of_target_ = c
        self.translation_of_averages_ = X_mean - c * np.dot(Y_mean, A) # This is slightly off  from R because the mean functions
        self.sum_of_squares_ = _ctrace(X_) + c * c * _ctrace(Y_) - 2 * c * np.sum(s)
        self.mse_ = self.sum_of_squares_/self.n_
        self.rmse_ = np.sqrt(self.mse_)
        self.residuals_ = np.sqrt(np.sum((self.X_ - self.Y_rotation_)**2, axis=1))
        self.quantiles_ = pd.Series(self.residuals_.quantile(q=[0,0.25, 0.5, 0.75, 1.0]).values, index=["Min", "1Q", "Median", "3Q", "Max"])
        
        #         self.mse_ = {
        #             "dimension_1": np.mean((Y_rotation[:,0] - Y_[:,0])**2),
        #             "dimension_2": np.mean((Y_rotation[:,1] - Y_[:,1])**2),
        #         }
        #         self.rmse_ = {
        #             "dimension_1": np.sqrt(self.mse_["dimension_1"]),
        #             "dimension_2": np.sqrt(self.mse_["dimension_2"]),
        #         }
        
    def summary(self):
        return pd.Series( 
            OrderedDict([ 
                ("Number of observations [n]", self.n_),
                ("Number of dimensions [k]", self.n_components),
                ("Rotation matrix [A]",self.rotation_),
                ("Sum of squares [ss]", self.sum_of_squares_),
                ("MSE", self.mse_),
                ("RMSE", self.rmse_),
                ("Translation of averages [b]", self.translation_of_averages_),
                ("Scaling of target [c]", self.scaling_of_target_),
                ("Residuals [resid]", self.residuals_.values),
                ("Quantiles of errors [Min,1Q,Med,3Q,Max]", self.quantiles_.values),
            ]),
            name=self.name,
        )
                

    def protest(
        self,
        n_iter=999,
        random_state=0,
        with_replacement=False,
        ):
        """
        https://rdrr.io/rforge/vegan/src/R/protest.R
        `protest` <- function (X, Y, scores = "sites", permutations = how(nperm = 999),...)
        {
            EPS <- sqrt(.Machine$double.eps)
            X <- scores(X, display = scores, ...)
            Y <- scores(Y, display = scores, ...)
            ## Centre and normalize X & Y here so that the permutations will
            ## be faster
            X <- scale(X, scale = FALSE)
            Y <- scale(Y, scale = FALSE)
            X <- X/sqrt(sum(X^2))
            Y <- Y/sqrt(sum(Y^2))
            ## Transformed X and Y will yield symmetric procrustes() and we
            ## need not specify that in the call (but we set it symmetric
            ## after the call).
            sol <- procrustes(X, Y, symmetric = FALSE)
            sol$symmetric <- TRUE
            sol$t0 <- sqrt(1 - sol$ss)
            N <- nrow(X)

            ## Permutations: We only need the goodness of fit statistic from
            ## Procrustes analysis, and therefore we only have the necessary
            ## function here. This avoids a lot of overhead of calling
            ## procrustes() for each permutation. The following gives the
            ## Procrustes r directly.
            procr <- function(X, Y) sum(svd(crossprod(X, Y), nv=0, nu=0)$d)

            permutations <- getPermuteMatrix(permutations, N)
            if (ncol(permutations) != N)
                stop(gettextf("'permutations' have %d columns, but data have %d observations",
                              ncol(permutations), N))
            np <- nrow(permutations)

            perm <- sapply(seq_len(np),
                           function(i, ...) procr(X, Y[permutations[i,],]))

            Pval <- (sum(perm >= sol$t0 - EPS) + 1)/(np + 1)

            sol$t <- perm
            sol$signif <- Pval
            sol$permutations <- np
            sol$control <- attr(permutations, "control")
            sol$call <- match.call()
            class(sol) <- c("protest", "procrustes")
            sol
        }
        """

        
        if not self.symmetric:
            warnings.warn("Protest on non-symmetrical Procrustes is experimental and should be consulted with the statistics community if used")
            
        # Get machine float error
        EPS = np.sqrt(np.finfo(float).eps)
        
        # Calculate correlation from sum of squares
        correlation_of_procrustes_rotation = np.sqrt(1 - self.sum_of_squares_)
        
        # Get X and Y values
        X_T = self.X_.values.T
        Y_ = self.Y_.values
        
        # Get integer index for permutations
        index = np.arange(0, self.n_)

        # Permute and run svd
        permutations = list()
        for rs in range(n_iter):
            index_permutation = np.random.RandomState(rs).choice(index, replace=with_replacement, size=self.n_) 
            XY = np.dot(X_T, Y_[index_permutation]) # crossprod(X,Y)
            U,s,Vh = np.linalg.svd(XY)
            permutations.append(np.sum(s))
        permutations = np.asarray(permutations)
        
        # Pval <- (sum(perm >= sol$t0 - EPS) + 1)/(np + 1)
        p_value = (np.sum(permutations >= correlation_of_procrustes_rotation - EPS) + 1)/(n_iter + 1)
        
        # Output
        return pd.Series(
            data=OrderedDict([
                ("Number of permutations [n_iter]",n_iter),
                ("With replacement", with_replacement),
                ("Random state",random_state),
                ("Sum of squares [M12 squared]", self.sum_of_squares_),
                ("Correlation of rotation",correlation_of_procrustes_rotation),
                ("P-value",p_value),
            ]), 
            name="Protest",
            dtype=object,
        )


def is_number(s):
    """判断字符串由数字组组成, 并且不是NaN

    Args:
        s (_type_): string

    Returns:
        _type_: bool
        
    # 测试字符串和数字
    print(is_number('foo'))   
    # False
    print(is_number('1'))    
    # True
    print(is_number('1.3'))  
    # True
    print(is_number('-1.37')) 
    # True
    print(is_number('1e3'))  
    # True
    print(is_number(math.nan))  
    # False
    """
    if s == None:
        return False
    
    # TODO:xiaojiao, 是否加上math.isfinite
    try:
        if isinstance(s, str):
            num = float(s.strip())
            # 去除NaN
            if math.isnan(num):
                return False
            return True
        # 如果是数字
        float(s)
        return True
    except ValueError:
        pass

    return False

# a = np.array([[1, 3], [1, 2], [1, 1], [2, 1]], 'd')
# b = np.array([[4, -2], [4, -4], [4, -6], [2, -6]], 'd')
# # mtx1, mtx2, disparity = procrustes(a, b)
# a = pd.DataFrame(a)
# b = pd.DataFrame(b)

# # round(disparity)
# test = Procrustes(a, b)


counts = defaultdict(lambda: defaultdict(int))

# 读取文件
# df = pd.read_csv('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count_particle.tsv',
#                  sep='\t',
#                  header=0)

df = pd.read_csv('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count.tsv',
                 sep='\t',
                 header=0)


# 读取文件 
with open('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count.tsv') as f:
    lines = f.readlines()
    # lines = f.readlines()
    headers = lines[0].split('\t')
    
    for line in lines[1:]:
        values = line.split('\t')
        gene = values[0] 
        for i, value in enumerate(values[1:]):
            sample = headers[i + 1]
            # 去除非数值字符
            if is_number(value):
                counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                # counts[gene][sample] = int(value)
  
# 提取基因名称 
# genes = [line.split('\t')[0] for line in lines[1:]]

# # 使用字典计数
# counts = {}
# for gene in genes:
#     counts[gene] = counts.get(gene, 0) + 1


print(counts)
# 使用Counter统计每个基因名称的计数
# counts = Counter(genes)

# 输出统计结果
print(counts)