from numpy import *
from numpy import linalg as LA
from sklearn.preprocessing import scale

# raw Data, including 3 character and 3 samples
# one line ,one sample; one column , one character
x = mat([[1,3, -7],[2,5,-14],[-3,-7,2]])

# matrix standardlized by columns
x_s = scale(x, with_mean=True, with_std=True, axis=0)
print("the standardedlized matrix: ", x_s);


# 协方差矩阵，先进行转置，因为这里的函数是行与行之间的方差
x_cov = cov(x_s.transpose())
# 输出协方差矩阵
print("协方差矩阵: ", x_cov, "\n");
# 是每一列的最主要特征吗？
eigVals,eigVects = LA.eig(x_cov)
print("协方差矩阵的特征值: ", eigVals);
print("协方差的特征向量(主成分): \n", eigVects, "\n")

# 找到最大的特征值，及其对应的特征向量
max_eigVal = -1
max_eigVal_index = -1

for i in range(0, eigVals.size):
    if(eigVals[i] > max_eigVal):
        max_eigVal = max_eigVal[i]
        max_eigVal_index = i

    eigVect_with_max_eigval = eigVals[:,max_eigVal_index]

# 输出最大的特征值以及对应的特征向量，也就是第一个主成分
print("最大的特征值:", max_eigVal)
print("最大特征值所对应的特征向量:", eigVect_with_max_eigval)

# 输出变换后的数据矩阵，注意，这里的三个值是表示三个样本的，而特征值从3维变为1维了
print("变换后的数据矩阵",x_s.dot(eigVect_with_max_eigval), "\n")










