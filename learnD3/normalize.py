import statistics

# 1. 首先判断data是否是空值
# min-max 归一化
import math
import csv
import numpy as np
import math
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# with open('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/Iris1.txt', newline = '') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter='\t')
#     for row in spamreader:
#         print(row)
        # print(', '.join(row))

filepath = f'C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/Iris1.txt'
# 读取csv文件
# 指定第一列作为索引
df = pd.read_table(filepath, sep = "\t", index_col = 0, header = 0)

# 提取整个DataFrame
data = df

# 对DataFrame进行归一化
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

# 生成新的DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)  

# 写回csv文件
normalized_df.to_csv('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/normalized_data.csv', index=False)



class DataNorm:
    def __init__(self, arr):
        self.arr = arr
        self.x_max = max(self.arr)
        self.x_min = min(self.arr)
        self.x_mean = sum(self.arr) / len(self.arr)
        self.x_std = np.std(self.arr) #标准差
    
    #1. Min-Max标准化
    def Min_Max(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x - self.x_min) / (self.x_max - self.x_min), 4))
        print("经过Min_Max标准化后的数据为：\n{}".format(arr_))
    
    #2. Z-Score标准化，Standard Score,基于原始数据的均值和标准差。
    def Z_Score(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round(((x - self.x_mean) / self.x_std), 4))
        print(self.x_std)
        print("经过Z_Score标准化后的数据为：\n{}".format(arr_))
      
    #3. 小数定标标准化，通过移动小数点的位置来进行数据的标准化。小数点移动的位数取决于原始数据中的最大绝对值。
    def DecimalScaling(self):
        arr_ = list()
        j = 1
        x_max = max([abs(i) for i in self.arr])
        while x_max / 10 >= 1.0:
            j+=1
            x_max = x_max / 10
        for x in self.arr:
            arr_.append(round(x / math.pow(10, j), 4))
        print("经过DecimalScaling标准化后的数据为：\n{}".format(arr_))
      
    #4. 均值归一化，通过原始数据中的均值、最大、最小值进行。
    def Mean(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x - self.x_mean) / (self.x_max - self.x_min), 4))
        print("经过Mean标准化后的数据为：\n{}".format(arr_))

    #5. 向量归一化，通过原始数据中的每一个值除以所有数据之和进行。
    def Vector(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round(x / sum(self.arr), 4))
        print("经过Vector标准化后的数据为：\n{}".format(arr_))

    #6. 指数转换
    def exponential(self):
        arr_1 = list()
        for x in self.arr:
            arr_1.append(round(math.log10(x) / math.log10(self.x_max), 4))
        print("经过指数转换法（log10）标准化后的数据为：\n{}".format(arr_1))

        arr_2 = list()
        sum_e = sum([math.exp(i) for i in self.arr])
        for x in self.arr:
            arr_2.append(round(math.exp(x) / sum_e , 4))
        print("经过指数转换法（softmax）标准化后的数据为：\n{}".format(arr_2))
        
        arr_3 = list()
        for x in self.arr:
            arr_3.append(round(1 / (1 + math.exp(-x)) , 4))
        print("经过指数转换法（sigmoid）标准化后的数据为：\n{}".format(arr_3))


a = DataNorm([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# a.Min_Max()
# a.exponential()
a.Z_Score()
a = DataNorm([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])

a.Z_Score()
def min_max_scaler(data):
    """
    data is array
    """
    min_value = min(data)
    max_value = max(data)
    range_ = max_value - min_value


    normalized_data = [0] * len(data)

    for value in data:
        normalized_value = (value - min_value) / range_
        normalized_data.append(normalized_value)

    return normalized_data

# mean 归一化
def mean_normalize(data):
    """
    Implement mean normalization algorithm.

    Mean normalization removes the average effect from the data by subtracting
    the mean value from each data point. It is commonly used as a preprocessing 
    step before further analysis.

    Parameters:
    data (list): Input data

    Returns: 
    list: Normalized data with mean centered to zero
    """

    length = len(data)
    mean = statistics.mean(data)

    normalized_data = [0] * length

    for value in data:
        normalized_value = value - mean
        normalized_data.append(normalized_value)

    return normalized_data

def MaxMinNormalization(x, min, max):
    """[0,1] normaliaztion"""
    x = (x - min) / (max - min)
    return x

def ZscoreNormalization(x, mean_, std_):
    """Z-score normaliaztion"""
    x = (x - mean_) / std_
    return x

def z_score_normalize(data):
    """
    使用Z-Score方法标准化数据

    Z-Score标准化通过减去平均值并除以标准差来进行转换,将分布中心移动到零点,
    且变异数调整为1。这使数据分布达到标准正态分布。

    参数:
    data(列表):原始数据

    返回: 
    列表:标准化后的数据,平均值为0,标准差为1
    """

    # 计算平均值和标准差
    mean = statistics.mean(data)
    std = statistics.stdev(data)
    std = statistics.variance(data)

    # 预分配输出数组
    normalized_data = [0] * len(data)

    # 循环计算每个样本
    for i in range(len(data)):

        # 计算Z-Score
        value = data[i]  
        z_score = (value - mean) / std  

        # 直接赋值结果
        normalized_data[i] = z_score

    return normalized_data

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data1 = [1, 0, 0, 0, 0]
# data2 = [2000, 0, 0, 0, 0]

# quantiles = statistics.mean(data)
# result1 = z_score_normalize(data1)
# result2 = z_score_normalize(data2)
# print(result1)
# print(result1)

