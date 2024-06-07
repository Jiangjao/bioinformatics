# !/usr/bin/python3
# --- encoding: utf-8 ---
import statistics
import math
import csv
from abc import ABC, abstractmethod
import random
import subprocess
import csv
import pandas as pd
from decimal import Decimal
from decimal import Decimal, getcontext

from functools import partial

# 设置精度
getcontext().prec = 128
# 参考资料
# https://blog.csdn.net/weixin_46713695/article/details/126301991
def get_nested_list_mean(df1_data, flag=True):
    len_df1 = len(df1_data)
    cols = len(df1_data[0]) - 1
    means = [None] * cols
    index  = 0
    # for i in range(len_df1):
        # col = [row[i] for row in df1_data]
    for col in df1_data:
        if len(col) != len_df1:
            pass
        # 如果第一列有列名，去除列名
        if flag:
            col.pop(0)
        print("col >>", col)
        col_with_number = list(map(eval, col))
        # col_with_number.pop(0)
        
        print(col_with_number)  
        if len(col_with_number) > 0:  
            mean = statistics.mean(col_with_number)  
            means[index] = mean
            index += 1
    
    # 去除空值
    means = [x for x in means if x]
    return statistics.mean(means)



def get_nested_list_std(df1_data, flag=True):
    len_df1 = len(df1_data)
    cols = len(df1_data[0]) - 1
    means = [None] * len_df1
    index  = 0
    # for i in range(len_df1):
        # col = [row[i] for row in df1_data]
    for col in df1_data:
        if len(col) != len_df1:
            pass
        # 如果第一列有列名，去除列名
        if flag:
            pass
    statistics.stdev(col)


# 原文链接：https://blog.csdn.net/weixin_42201701/article/details/103408370
def IntervalMappingAfterNormalization(data, data_min, data_max, MIN, MAX):
    """
    归一化映射到任意区间
    :param data: 数据 matrix
    :param MIN: 目标数据最小值
    :param MAX: 目标数据最小值
    :return:
    """
    
    # 当前数据最大值
    d_min = data_min
    # 当前数据最小值 
    d_max = data_max   
    
    len_df1 = len(data)
    cols = len(data[0]) - 1
    means = [None] * cols
    index  = 0
    # for i in range(len_df1):
        # col = [row[i] for row in df1_data]
    colnames = None
    for col in data:
        if len(col) != len_df1:
            pass
        # 如果第一列有列名，去除列名
        if True:
            colnames = col.pop(0)
        # print("col >>", col)
        col_with_number = list(map(eval, col))
        # col_with_number.pop(0)
        
        # print(col_with_number)  

        d_max = max(col)
        d_min = max(col)
        # 去除空值
        mean = [MIN + (MAX - MIN) / (d_max - d_min) * (x - d_min) for x in col_with_number if x]
        means[index] = mean
        index += 1
    # return statistics.mean(means)
    # return MIN + (MAX - MIN) / (d_max - d_min) * (data - d_min)
    return means

def transform_nested_list(data):
    """
    归一化映射到任意区间
    :param data: 数据 matrix

    :return matrix:
    """
    # lists = [[1,2,3], [4,5,6]]

    try:
        transposed = list(map(list, zip(*data)))
    except Exception as error:
        raise ValueError("输入的数据有问题")
    
    return transposed

def interval_mapping_normalization_with_nested_matrix(data, data_min, data_max, MIN, MAX):
    """
    归一化映射到任意区间
    :param data: 数据 matrix
    :param MIN: 目标数据最小值
    :param MAX: 目标数据最小值
    :return:
    """
    
    # 当前数据最大值
    d_min = data_min
    # 当前数据最小值 
    d_max = data_max   
    
    len_df1 = len(data)
    cols = len(data[0]) - 1
    means = [None] * len_df1
    index  = 0
    # for i in range(len_df1):
        # col = [row[i] for row in df1_data]
    colnames = None
    for row in data:
        if len(row) != len_df1:
            pass
        # 判断是否空行, None等等
        if len(row) == 0:
            continue
        # 如果第一列有列名，去除列名
        # if False:
        #     colnames = col.pop(0)
        # print("col >>", col)
        # col_with_number = list(map(eval, col))
        # col_with_number.pop(0)
        
        # print(col_with_number)  
        d_max = max(row)
        d_min = min(row)
    
        # 去除空值
        mean = [MIN + (MAX - MIN) / (d_max - d_min) * (x - d_min) for x in row if x]
        means[index] = mean
        index += 1
    # return statistics.mean(means)
    # return MIN + (MAX - MIN) / (d_max - d_min) * (data - d_min)
    means = [x for x in means if x is not None]
    return means



# data的数据性描述
class DataWithDescription:
    """
    嵌合阿拉伯数字矩阵data
    
    data的数据性描述
    """
    def __init__(self, data):
        # 
        self.data = data
        self.data_min = None
        self.data_max = None
        self.data_mean = None
        self.data_std = None
        self.data_variance = None
        self.data_median = None
        self.data_skew = None
        self.data_kurtosis = None
        self.data_var = None
        self.data_describe = None
        self.data_range = None
        self.data_quantile = None
        self.data_percentile = None
        self.data_mode = None
        self.data_unique = None
        self.data_count = None
        self.data_count_distinct = None
        self.data_count_null = None
        self.data_count_not_null = None

    def iter_data(self):
        pass

    @classmethod
    def transform_nested_list(clwws, data):
        """
        归一化映射到任意区间
        :param data: 数据 matrix

        :return matrix:
        """
        # lists = [[1,2,3], [4,5,6]]

        try:
            transposed = list(map(list, zip(*data)))
        except Exception as error:
            raise ValueError("输入的数据有问题")

        return transposed
    
    def calculate_stats(self):
        """
        计算描述统计量        
        """
        self.data = self.transform_nested_list(self.data)
        
        self.data_min = min(self.flatten_data())
        self.data_max = max(self.flatten_data()) 
        self.data_mean = statistics.mean(self.flatten_data())
        
        #计算其他统计量
        
        return self

    def flatten_data(self):
        """
        展平嵌套列表
        """
        flat_list = [item for sublist in self.data for item in sublist]
        return flat_list

class Normalization(ABC):
    @abstractmethod
    def transform(self, data):
        pass

# #  MinMaxNormalizer类
# # 0 - 1 归一化
class MinMaxNormalizer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.transform_nested_list(data.data)
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象

        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        MIN = 0
        MAX = 1
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            if len(row) != len_df1:
                pass
            # 判断是否空行, None等等
            # if len(row) == 0:
            #     continue
            # 如果第一列有列名，去除列名
            # if False:
            #     colnames = col.pop(0)
            # print("col >>", col)
            # col_with_number = list(map(eval, col))
            # col_with_number.pop(0)
            
            # print(col_with_number)  

            d_max = max(row)
            d_min = min(row)
            # 去除空值
            mean = [MIN + (MAX - MIN) / (d_max - d_min) * (x - d_min) for x in row]
            # means[index] = mean
            results[index] = mean
            index += 1
        # return statistics.mean(means)
        # return MIN + (MAX - MIN) / (d_max - d_min) * (data - d_min)
        results = [x for x in results]
        return results

# #  MinMaxNormalizer类
# # -1 - 1 归一化
class meanNormalizer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # print(self.data)
        print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            if len(row) != len_df1:
                pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
            # 如果第一列有列名，去除列名
            # if False:
            #     colnames = col.pop(0)
            # print("col >>", col)
            # col_with_number = list(map(eval, col))
            # col_with_number.pop(0)
            
            # print(col_with_number)  
            data_min = min(row)
            data_max = max(row)
            data_interval = data_max - data_min
        
            # 去除空值
            mean = [(x - data_min) / data_interval for x in row if x]
            results[index] = mean
            index += 1
        # return statistics.mean(means)
        # return MIN + (MAX - MIN) / (d_max - d_min) * (data - d_min)
        results = [x for x in results if x is not None]
        return results


# ZScoreNormalizer类  
class ZScoreNormalizer(Normalization):

    def transform(self, data):
        # 放大精度10000
        scale = 1000000
        data_input = data.data

        # data_input = [ [float(x) * scale for x in line] for line in data_input]
        # [[Decimal(x) for x in line] for line in data]
        # data_mean = data.data_mean * scale
        # data_std = data.data_std * scale

        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        
        for row in data_input:
            # row = []
            # for x in line:
            #     row.append(Decimal(float(x)) * Decimal(scale))
            print("row >>>", row)
            # row = [Decimal(x) * Decimal(scale) for x in rows]
            # row = rows
            # if len(row) != len_df1:
            #     pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
        
            data_mean = statistics.mean(row)
            # data_mean = math.fsum(row) / len(row)
            # statistics.m
            data_std = statistics.stdev(row)
            # statistics.
            # 去除空值
            # z = (x - mean) / std
            mean = [Decimal( Decimal(x) - Decimal(data_mean)) / Decimal(data_std)  for x in row if x]
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x  for x in means if x is not None]
        return means

# LogNormalizer类data_max
class Log1pNormalizer(Normalization):

    def transform(self, data):
        data_input = data.data
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            # if len(row) != len_df1:
            #     pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
        
            # 去除空值
            # z = (x - mean) / std
            mean = [math.log1p(x) for x in row if x]
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return means

class Log2Normalizer(Normalization):

    def transform(self, data):
        data_input = data.data
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            # if len(row) != len_df1:
            #     pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
        
            # 去除空值
            # z = (x - mean) / std
            try:
                mean = [math.log2(x) for x in row if x]
            except ValueError:
                raise ValueError(f'{row}, 有0值')
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return means


class Log10Normalizer(Normalization):

    def transform(self, data):
        data_input = data.data
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            # if len(row) != len_df1:
            #     pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
        
            # 去除空值
            # z = (x - mean) / std
            try:
                mean = [math.log10(x) for x in row if x]
            except ValueError:
                raise ValueError(f'{row}, 有0值')
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return means


# # 5. center 中心值归一化
class CenterNormalizer(Normalization):
    
    def transform(self, data):
        # mean = np.mean(data)
        data_input = data.data
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            if len(row) != len_df1:
                pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
            
            data_mean = statistics.mean(row)
            # 去除空值
            # z = (x - mean) / std
            mean = [x - data_mean for x in row if x]
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return means
        return (data - mean)

# #  6. 帕莱托分布 归一化
class ParetoNormalizer(Normalization):
    
    def transform(self, data):
        data_input = data.data
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            if len(row) != len_df1:
                pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue
            
            data_mean = statistics.mean(row)
            data_std = statistics.stdev(row)
            # 去除空值
            # z = (x - mean) / std
            mean = [(x - data_mean) / data_std for x in row if x]
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return means
        # mean = data.mean()
        # std = data.std()

        # normalized = (data - mean) / std
        # normalized = (data - min_) / (max_ - min_)  
        # normalized = 1 - (1/normalized)**scale
        # return normalized

# 8. 相对丰度按行计算
class RelativeAbundanceNormalizer(Normalization):

    def transform(self, data):
        data_input = transform_nested_list(data.data)
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0]) - 1
        means = [None] * len_df1
        index  = 0
        # for i in range(len_df1):
            # col = [row[i] for row in df1_data]
        colnames = None
        for row in data_input:
            # if len(row) != len_df1:
            #     pass
            # 判断是否空行, None等等
            if len(row) == 0:
                continue

            # 去除空值
            # z = (x - mean) / std
            try:
                row_total = math.fsum(row)
                mean = [x / row_total for x in row if x]
            except ValueError:
                raise ValueError("数据格式错误，请参考示例文件检查数据文件是否正确。")
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return transform_nested_list(means)

# 工厂
# 其他归一化类

class NormalizationFactory:

    normalizer_map = {
        'min-max': MinMaxNormalizer,
        'Z-score': ZScoreNormalizer,
        'log(1+x)': Log1pNormalizer,
        'log2(x)': Log2Normalizer,
        'log10(x)': Log10Normalizer,
        'center': CenterNormalizer,
        'Pareto': ParetoNormalizer,
        'mean':meanNormalizer,
        '相对丰度': RelativeAbundanceNormalizer
    }

    def get_normalizer(self, name):
        normalizer_class = self.normalizer_map[name]
        return normalizer_class()

# author by : www.runoob.com
# https://www.runoob.com/python3/python3-check-is-number.html
def is_number(s):
    """判断字符串由数字组组成

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
    """
    try:
        float(s.strip())
        return True
    except ValueError:
        pass
 
    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (TypeError, ValueError):
    #     pass
 
    return False


def batch_effect_rectification2(input_file, contained_name_with_colname_rowname, parametric_method):
    # 参数判断
    if not isinstance(input_file, str):
        raise ValueError("输入文件不是字符串")
    if not isinstance(contained_name_with_colname_rowname, str):
        raise ValueError("contained_name_with_colname_rowname 不是字符串")
    if not isinstance(parametric_method, str):
        raise ValueError("parametric_method 不是字符串")
    
    choices = ["行名", "列名", "都有", "都没有"]
    parametric_method_choices = ["min-max", "Z-score", "mean", "Pareto", "center", "log(1+x)", "log2(x)", "log10(x)", "相对丰度"]

    if contained_name_with_colname_rowname not in choices:
        raise ValueError("contained_name_with_colname_rowname 参数错误") 
    if parametric_method not in parametric_method_choices:
        raise ValueError("parametric_method 参数错误")
    # assert parametric_method in parametric_method_choices, "parametric_method 参数错误"

    # print(f"contained_name_with_colname_rowname <{contained_name_with_colname_rowname}> >>>", contained_name_with_colname_rowname in choices)

    # 将表格字符串转换为列表形式

    with open(input_file) as f:
        input_file = f.read()
    data = [line.split('\t') for line in input_file.split('\n') if line]

    # reader = csv.reader(input_file, delimiter='\t')

    # print("reader >>>", reader)
    # TODO:xiaojiao, 去除字符串中的空格
    len_df1 = len(data)
    length_cols = len(data[0]) - 1
    rownames = [None] * len_df1
    colnames = [None] * length_cols
    # colnames = data.pop(0)
    index = 0
    
    # TODO:xiaojiao, 增加contained_name_with_colname_rowname与文件行列情况不对应的状态
    # 1. 都有
    if contained_name_with_colname_rowname == "都有":
        index = 0
        # print(">>> data, data", data)
        colnames = data.pop(0)
        for line in data:
            # print("line >>> before", line)
            rownames[index] = line.pop(0)
            index += 1
            # print("line >>> line", line)
        # print("data >>>", data)
        # data = [[float(x) for x in line] for line in data]
        # interval_mapping_normalization_with_nested_matrix(data)
    elif contained_name_with_colname_rowname == "行名":

        for line in data:
            rownames[index] = line.pop(0)
            index += 1
        # data = [[float(x) for x in line] for line in data]
        # interval_mapping_normalization_with_nested_matrix(data)
    elif contained_name_with_colname_rowname == "列名":
        colnames = data.pop(0)
        # for line in data:
        #     rownames[index] = line.pop(0)
        # data = [[float(x) for x in line] for line in data]
    
    elif contained_name_with_colname_rowname == "都没有":

        # colnames = data.pop(0)
        index = 0
        # for line in data:
        #     rownames[index] = line.pop(0)
        # data = [[float(x) for x in line] for line in data]

    # 捕获 ValueError
    try:
        data = [[Decimal(x) for x in line] for line in data]
    except ValueError:
        raise ValueError("数据格式错误，<em>是否包含行列</em>，请参考示例文件检查输入文件格式是否正确。")
    
    # 判断是否是矩阵，不包含空值
    for row in data:
        # if None in row:
        #     raise ValueError("数据格式错误，请参考示例文件检查数据文件是否正确。")
        if len(row) != length_cols:
            raise ValueError("数据格式错误, 包含空值, 请参考示例文件检查数据文件是否正确。")
    # 去除None
    rownames = [x for x in rownames if x is not None]
    # print(data)
    print("sucess")
    # 变成一维数组
    data2 = [Decimal(x) for line in input_file.split('\n')
                 for x in line.split('\t') if line
                 if is_number(x)]

    data_std = statistics.stdev(data2)
    data_mean = statistics.mean(data2)
    data_variance = statistics.variance(data2)
    data_max = max(data2)
    data_min = min(data2)

    print(data_max, data_min, ">>>")
    # data = transform_nested_list(data)
    data_with_description =  DataWithDescription(data)
    data_with_description.data_max = data_max
    data_with_description.data_min = data_min
    data_with_description.data_mean = data_mean
    data_with_description.data_std = data_std
    data_with_description.data_variance = data_variance
    data_with_description.rownames = rownames
    data_with_description.colnames = colnames

    # print(">>> rownames", rownames)

    # 调用
    factory = NormalizationFactory()
    norm = factory.get_normalizer(parametric_method)
    result = norm.transform(data_with_description)

    # norm.transform(data)
    # print("norm >>>", result)
    temp = transform_nested_list(result)
    # 将结果转换为制表符分隔的字符串
    # insert(0,)
    # result_str = ''.join(['\t'.join(str(row)) for row in colnames]) + '\n'

    print("temp >>>", temp)
    colnames = [str(x) if x else "" for x in colnames]
    if contained_name_with_colname_rowname == "行名" or contained_name_with_colname_rowname == "都有":
        index = 0
        for row in temp:
            row.insert(0, rownames[index]) 
            index += 1
            # print(">>> row", row)
    if contained_name_with_colname_rowname == "列名" or contained_name_with_colname_rowname == "都有":
        temp.insert(0, colnames)


    result_str = '\n'.join(['\t'.join(str(row)) for row in temp]) + '\n'
    # string = '\n'.join(['\t'.join([str(x) for x in row]) for row in temp])
    string = '\n'.join(['\t'.join([str(x) if x else "" for x in row])
                     for row in temp])

    # print("string >>>", string)
    print("temp >>>", temp)
    return dict(
        content = string,
        type="table",
        name="归一化后的表格"
    )



if __name__ == "__main__":
    # 1. 首先判断data是否是空值
    # 读取csv文件 
    filepath = f'C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/Iris1.txt'

    # 指定第一列作为索引
    df = pd.read_table(filepath, sep = "\t", index_col = 0, header = 0)
    batch_effect_rectification2('C:/Users/Cherry/Downloads/dynamic_grid_heatmap_with_mantel_test_env_file (3).txt',
                # "C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/",
                contained_name_with_colname_rowname ="都有",
                parametric_method="min-max")

# log 转换是没有问题的...
# TODO:xiaojiao 修复其他的算法