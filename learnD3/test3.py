import numpy as np
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

import pandas as pd
data = [['1', '', '']]
rows_length = len(data)

data_input = [['1', '', '']]



len_df1 = len(data_input)
cols_length = len(data_input[0]) - 1
results = [None] * len_df1
data_min = 1
# 列表推导式生成空矩阵
flag_mat = [
    [None] * cols_length for _ in range(rows_length)
]

na_value = ""
# 重写这个
# 3. 对缺失值进行标记
for row_index in range(0, len_df1):
    if 2:
        # row = [Decimal(x) for x in data_input[row_index] if is_number(x)]
        min_value_in_row = data_min
    for v in range(0, cols_length):
        # if min_value_in_row in data:
        if isinstance(flag_mat[row_index][v], float):
            pass
        elif str(flag_mat[row_index][v]).strip() == str(na_value):
            flag_mat[row_index][v] = min_value_in_row

print(flag_mat)


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
        
        
from tqdm import trange

# https://stackoverflow.com/questions/70870829/how-to-plot-rs-veganprocrustes-using-python-scipy-numpy-and-matplotlib
def protest(X, Y, no_permutations=999, with_replacement=False):
    '''Performs procrustean test (PROTEST).

    H_0: "X and Y are no more related than random datasets would be."
    
    Args:
        X (np.ndarray):             Matrix of shape (n x p11), where n is the number of observations
        Y (np.ndarray):             Matrix of shape (n x p12)
        no_permutations (int):      Number of permutations to consider
        with_replacement (bool):    If set to True, permutations are sampled with replacement.

    Returns:
        test_statistic (float):          Procrustean correlation coefficient
        p_value (float):    P-Value of PROTEST
        RSS (float):        Residual Sum of Squares of prucrustes rotations

    References:
        Gower & Dijksterhuis (2004):    "Procrustes Problems"
        Gower (1971):                   "Statistical methods of comparing different multivariate analyses 
                                            of the same data", p. 138-149
        Peres-Neto & Jackson (2001):    "How well do multivariate data sets match? The advantages of 
                                            a Procrustean superimposition approach over the Mantel test"   
    '''
    n = X.shape[0]
    assert n == Y.shape[0], 'X has to be of shape (n x p1) and Y has to be of shape (n x p2).'

    # Get machine float error
    EPS = np.sqrt(np.finfo(float).eps)

    # # standardize the matrices using Gower-Transformation (Gower 1971)
    X, Y = gower_trafo(X), gower_trafo(Y)

    # calculate test statistic & residual sum of squares
    test_statistic = procrustes_corr(X, Y)
    RSS = np.sum(X**2) + np.sum(
        Y**2) - 2 * test_statistic  # c.f. Gower & Dijksterhuis (2004), equation 4.3

    # Get integer index for permutations
    index = np.arange(0, n)

    # Permute and calculate goodness of fit
    permutations = list()
    for rs in trange(no_permutations):
        permutated_idx = np.random.RandomState(rs).choice(index, replace=with_replacement, size=n)
        corr = procrustes_corr(X[permutated_idx], Y)
        permutations.append(corr)
    permutations = np.array(permutations)

    p_value = (np.sum(permutations >= test_statistic - EPS) + 1) / (no_permutations + 1)

    # Print Output
    print(f'Performed PROTEST with {no_permutations} permutations.')
    print(f'Procrustean correlation coefficient: {test_statistic}')
    print(f'p-Value: {p_value}')
    print(f'Residual Sum of Squares: {RSS}')

    return test_statistic, p_value, RSS


def procrustes_corr(X, Y):
    '''Calculates the procrustean correlation coefficient.
    
    Args:
        X (np.ndarray):   Gower-transformed Matrix of shape (n x p1), where n is the number of observations
        Y (np.ndarray):   Gower-transformed Matrix of shape (n x p2)

    Returns:
        corr (float):    The goodness of fit of the orthogonal procrustes rotation. Procrustean form of Corelation coefficient.

    References:
        Peres-Neto & Jackson (2001):    "How well do multivariate data sets match? The advantages of 
                                        a Procrustean superimposition approach over the Mantel test"       
    '''
    XY = np.dot(X.T, Y)
    _, s, _ = np.linalg.svd(XY)

    # for performing PROTEST (Peres-Neto & Jackson 2001)
    corr = np.trace(np.diag(s))

    return corr


def gower_trafo(A):
    '''Standardizes Matrix A using Gower-Transformation.

    Args:
        A (np.ndarray):     Matrix of shape (n x p), where n is the number of observations

    Returns:
        A (np.ndarray):     Standardized Matrix A

    References:
        Gower (1971):       "Statistical methods of comparing different multivariate analyses 
                             of the same data", p. 138-149
    '''
    A = A - A.mean(axis=0, keepdims=True)
    A = A / np.sqrt(np.sum(A**2))
    return A


# 教程1: https://blog.csdn.net/woodcorpse/article/details/106554527
# 教程2：https://blog.csdn.net/baidu_38172402/article/details/82750070

# 
a = np.array([[1, 3], [1, 2], [1, 1], [2, 1]], 'd')
b = np.array([[4, -2], [4, -4], [4, -6], [2, -6]], 'd')
# mtx1, mtx2, disparity = procrustes(a, b)
a = pd.DataFrame(a)
b = pd.DataFrame(b)

# 计算pca or pcoa
# https://github.com/JBris/multivariate_analysis_examples/blob/master/scripts/user/python/canonical_correlation_and_rda.py
# from skbio.stats.ordination import rda

log = r"""Compute redundancy analysis, a type of canonical analysis.

    It is related to PCA and multiple regression because the explained
    variables `y` are fitted to the explanatory variables `x` and PCA
    is then performed on the fitted values. A similar process is
    performed on the residuals.

    RDA should be chosen if the studied gradient is small, and CCA
    when it's large, so that the contingency table is sparse"""
# rda = redundancy analysis
# normally RDA is used for “constrained ordination” (ordination w/covariates or predictor)
# without predictors, RDA is the same as PCA
# in vegan, givig the function rda() dataframe without predictors runs a PCA very simiar to princomp
# pca = PCA(n_components=2)
# pca.fit(a)
import numpy as np
from sklearn.cross_decomposition import CCA

# Example data (replace with your own data)
X = np.random.rand(100, 3)  # Explanatory matrix (n x p)
Y = np.random.rand(100, 5)  # Response matrix (n x m)

# Fit RDA model
rda = CCA(n_components=3)
rda.fit(X, Y)

# Get canonical axes
Z = rda.transform(X)

# Interpret the results
print("Canonical axes (Z):")
print(Z)

# round(disparity)
test = Procrustes(a, b)

print(test)