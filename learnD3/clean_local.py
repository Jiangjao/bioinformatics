# !/usr/bin/python3
# --- encoding: utf-8 ---
import statistics
import math
from abc import ABC, abstractmethod
import random
import subprocess
from decimal import Decimal, getcontext
import platform
from functools import partial
import csv

# 设置精度
getcontext().prec = 64

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


# 原文链接：https://blog.csdn.net/weixin_42201701/article/details/103408370


# data的数据性描述
class DataWithDescription:
    """
    嵌合阿拉伯数字矩阵data
    
    data的数据性描述
    
    如果是但列数据，则data是一个列表，列表中的元素是数值
    """
    def __init__(self, data):
        self.data = self.transform_nested_list(data)
        self.data_flag = None
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
    def transform_nested_list(cls, data):
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

    @classmethod
    def filter_data_by_row(cls, data, threshold=0.5):
        # data = [[1, 'Na', 2], 
        #     [3, 'NaN', 5], 
        #     [6, 7, 8]]

        # threshold = 0.8

        new_data = []
        for i, row in enumerate(data):

            num_count = 0
            for v in row:
                if isinstance(v, (int, float)):
                    num_count += 1

            row_length = len(row)
            num_ratio = num_count/row_length

            if num_ratio >= threshold:
                new_data.append(row)


        print(new_data)
        return new_data

class Normalization(ABC):
    @abstractmethod
    def transform(self, data):
        pass

# #  MinMaxNormalizer类
# # 0 - 1 归一化
class MinFilledGlobalImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        # data_input = [['1', '', '']]
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)

        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) 
        results = [None] * len_df1
        index  = 0
        MIN = 0
        MAX = 1
        colnames = None

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


        # results = [x for x in results]
        # return transform_nested_list(results)
        return flag_mat

# #  MinMaxNormalizer类
# # -1 - 1 归一化
class MaxFilledGlobalImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        colnames = None

        # 重写这个
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1 - 1):
            if 0:
                pass
            elif 2:
                row = [Decimal(x) for x in data_input[row_index] if is_number(x)]
                min_value_in_row = data_max
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = min_value_in_row


        # results = [x for x in results]
        # return transform_nested_list(results)
        return flag_mat

# ZScoreNormalizer类
class MinFilledByLineImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0

        colnames = None

        # 重写这个
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1 - 1):
            if 0:
                pass
            elif 2:
                row = [Decimal(x) for x in data_input[row_index] if is_number(x)]
                min_value_in_row = min(row)
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = min_value_in_row


        return flag_mat

# LogNormalizer类data_max
class MaxFilledByLineImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        MIN = 0
        MAX = 1
        colnames = None

        # 重写这个
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1 - 1):
            if 0:
                pass
            elif 2:
                row = [Decimal(x) for x in data_input[row_index] if is_number(x)]
                min_value_in_row = max(row)
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = min_value_in_row


        # results = [x for x in results]
        # return transform_nested_list(results)
        return flag_mat

class AvgFilledByLineImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        colnames = None

        # 重写这个
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1 - 1):
            if 0:
                pass
            if 2:
                row = [Decimal(x) for x in data_input[row_index] if is_number(x)]
                flag_value_in_row = statistics.mean(row)
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = flag_value_in_row


        # results = [x for x in results]
        # return transform_nested_list(results)
        return flag_mat


class AvgFilledGlobalImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean

        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        colnames = None

        # 重写这个
        
        
        # 添加remove 矩阵的index
        remove_matrix_index = []
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1):
            if 0:
                pass
            if 2:
                row = [x for x in data_input[row_index] if is_number(x)]

                # row_filling_rate = Decimal((len(row) - 1) / cols_length)
                # if row_filling_rate < len_df1:
                #     # 
                #     data.rownames.pop(row_index)
        
                #     # 标记矩阵去除这一行
                #     remove_matrix_index.append(row_index)
                #     # [12].po
                #     # 处理
                #     continue
                #     pass
                flag_value_in_row = data_mean
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = flag_value_in_row

        for index in remove_matrix_index:
            flag_mat.pop(index)
        # results = [x for x in results]
        # return transform_nested_list(results)
        return flag_mat


class ZeroFilledGlobalImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = 0

        data_interval = data_max - data_min
        # print(self.data)
        # print("data description >>>", data_max, data_min)
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0]) - 1
        results = [None] * len_df1
        index  = 0
        colnames = None

        # 重写这个
        
        
        # 添加remove 矩阵的index
        remove_matrix_index = []
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1):
            if 0:
                pass
            if 2:
                row = [x for x in data_input[row_index] if is_number(x)]

                # row_filling_rate = Decimal((len(row) - 1) / cols_length)
                # if row_filling_rate < len_df1:
                #     # 
                #     data.rownames.pop(row_index)
        
                #     # 标记矩阵去除这一行
                #     remove_matrix_index.append(row_index)
                #     # [12].po
                #     # 处理
                #     continue
                #     pass
                flag_value_in_row = data_mean
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = flag_value_in_row

        for index in remove_matrix_index:
            flag_mat.pop(index)
        # results = [x for x in results]
        # return transform_nested_list(results)
        return flag_mat


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
            mean = [x - data_mean for x in row if x is not None]
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
            mean = [(x - data_mean) / data_std for x in row]
            means[index] = mean
            index += 1
        # print(f'Z-score of {x} is {z}')
        means = [x for x in means if x is not None]
        return means


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
                mean = [Decimal(x) / Decimal(row_total) for x in row if x is not None]
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
        'min': MinFilledGlobalImputer,
        'max':MaxFilledGlobalImputer,
        'colMin': MinFilledByLineImputer,
        'colMax': MaxFilledByLineImputer,
        'colAvg': AvgFilledByLineImputer,
        'avg': AvgFilledGlobalImputer,
        'center': CenterNormalizer,
        'Pareto': ParetoNormalizer,
        '0': ZeroFilledGlobalImputer
        # '相对丰度': RelativeAbundanceNormalizer
    }

    def get_normalizer(self, name):
        normalizer_class = self.normalizer_map[name]
        return normalizer_class()

# author by : www.runoob.com
# https://www.runoob.com/python3/python3-check-is-number.html
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
        float(s)
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


def filter_data_by_row(data, threshold=0.5):
    threshold = float(threshold)
    new_data = []
    for i, row in enumerate(data):

        num_count = 0
        for v in row:
            if is_number(v):
                num_count += 1
            # if isinstance(v, (int, float)):
            #     num_count += 1

        row_length = len(row)
        if row_length == 0:
            raise ValueError("输入文件有问题")

        num_ratio = num_count / row_length

        non_num_ratio = 1 - num_ratio
        if num_ratio >= threshold:
            new_data.append(i)

    # print(new_data)
    return new_data

# filter_data_by_row(data, 1)

def normalization_or_standardizatation(input_file, contained_name_with_colname_rowname, parametric_method, na_type, na_value, missing_value_threshold):

    # 1. 设置字符串


    # 1.1 解析输入的缺失替换值
    if na_type == "自定义":
        na_value = na_value.strip()
    if na_value == None:
        na_value = na_type

    if na_value == "空值":
        # TODO:xiaojiao ，需要添加空格的校验
        na_value = ""

    if platform.system() == 'Windows':
        # 调试使用, debug
        if isinstance(input_file, str):
            with open(input_file) as f:
                input_file = f.read()
        print('Windows')
    elif platform.system() == 'Linux':
        print('Linux')
    elif platform.system() == 'Darwin':
        print('Mac')
    else:
        print('Other')

    # 2. 设定缺失值编码
    # 2. 设定缺失值编码
    # na_value = na_type
    # na_value = None
    print(f"na_type<na_value> >>>", na_value)

    # na_value = na_type

    # 5-6. 计算/移除缺失率高行列

    print("enter normalization bakend")
    # 参数判断
    if not isinstance(input_file, str):
        raise ValueError("输入文件不是字符串")
    if not isinstance(contained_name_with_colname_rowname, str):
        raise ValueError("contained_name_with_colname_rowname 不是字符串")
    if not isinstance(parametric_method, str):
        raise ValueError("parametric_method 不是字符串")
    
    choices = ["行名", "列名", "都有", "都没有"]
    parametric_method_choices = ['min', 'max', 'avg', 'colMax', 'colMin', 'colAvg', 'colMedian', 'rowMin', 'rowAvg', 'rowMedian', '0']

    if contained_name_with_colname_rowname not in choices:
        raise ValueError("contained_name_with_colname_rowname 参数错误")
    if parametric_method not in parametric_method_choices:
        raise ValueError("parametric_method 参数错误")

    # print(f"contained_name_with_colname_rowname <{contained_name_with_colname_rowname}> >>>", contained_name_with_colname_rowname in choices)

    # 将表格字符串转换为列表形式
    data = [line.split('\t') for line in input_file.split('\n') if line]

    # print("reader >>>", reader)
    # TODO:xiaojiao, 去除字符串中的空格
    len_df1 = len(data)
    length_cols = len(data[0]) - 1
    rownames = [None] * len_df1
    colnames = [None] * length_cols
    # colnames = data.pop(0)
    index = 0
    
    # 1.2 产生标记矩阵
    # 获取行列数
    rows_length = len(data) 
    cols_length = len(data[0]) - 1

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
    # try:
    #     data = [[Decimal(x) for x in line] for line in data]
    # except Exception as error:
    #     raise ValueError("数据格式错误，<em>是否包含行列</em>，请参考示例文件检查输入文件格式是否正确。")
    
    # 判断是否是矩阵，不包含空值
    # for row in data:
    #     # if None in row:
    #     #     raise ValueError("数据格式错误，请参考示例文件检查数据文件是否正确。")
    #     if len(row) != length_cols:
    #         raise ValueError("数据格式错误, 包含空值, 请参考示例文件检查数据文件是否正确。")
    # 去除None
    rownames = [x for x in rownames if x is not None]
    # print(data)
    # print("sucess")
    # 变成一维数组

    # 2.3 去除缺失值阈值高的row
    filter_index_list =  filter_data_by_row(data, 0)
    new_data = [row for i, row in enumerate(data) if i in filter_index_list]
    data = new_data

    new_row = [row for i, row in enumerate(rownames) if i in filter_index_list]
    rownames = new_row
    print("filter_index_list >>>", filter_index_list)

    # 获得新行列数
    # 1.2 产生标记矩阵
    # 获取行列数
    rows_length = len(data)
    
    # 列表推导式生成空矩阵
    flag_mat = [
        [None] * cols_length for _ in range(rows_length)
    ]

    print(flag_mat)
    # cols_length = len(data[0]) - 1
    # 3. 对缺失值进行标记
    for row in range(0, rows_length):
        for v in range(0, cols_length):
            if data[row][v].strip() == str(na_value):
                flag_mat[row][v] = str(na_value).strip()
            else:
                # 数组深层拷贝
                # TODO:xiaojiao, 原生还是这个数组深层拷贝性能好些？
                flag_mat[row][v] = data[row][v]
            # 替换成数字
            if is_number(data[row][v]):
                data[row][v] = float(data[row][v])
                flag_mat[row][v] = float(data[row][v])
            else:
                data[row][v] = None

    # data2 = [Decimal(x) for line in input_file.split('\n')
    #              for x in line.split('\t') if line
    #              if is_number(x)]
    # 使用一层列表推导式嵌套一个循环
    data2 = [Decimal(item) for row in data
                for item in row if is_number(item)]
    print("data2 >>>", data2)
    # data_std = statistics.stdev(data2)
    data_mean = statistics.mean(data2)
    # data_variance = statistics.variance(data2)
    data_max = max(data2)
    data_min = min(data2)

    data_with_description = DataWithDescription(data)
    data_with_description.na_value = na_value
    data_with_description.data_flag = flag_mat
    data_with_description.data_max = data_max
    data_with_description.data_min = data_min
    data_with_description.data_mean = data_mean
    # data_with_description.data_std = data_std
    # data_with_description
    # data_with_description.data_variance = data_variance
    data_with_description.rownames = rownames
    data_with_description.colnames = colnames

    print(">>> rownames", rownames)

    # print("len_df1 >>>", df1_data)
    print("parametric_method >>>", parametric_method)

    # 调用
    factory = NormalizationFactory()
    norm = factory.get_normalizer(parametric_method)
    result = norm.transform(data_with_description)

    # # norm.transform(data)
    # # print("norm >>>", result)
    temp = transform_nested_list(result)
    print(temp)
    # # 将结果转换为制表符分隔的字符串
    # # insert(0,)
    
    # print("colnames >>>", colnames)
    colnames = [str(x) if x else "" for x in colnames]
    if contained_name_with_colname_rowname == "行名" or contained_name_with_colname_rowname == "都有":
        index = 0
        for row in temp:
            row.insert(0, rownames[index]) 
            index += 1
            # print(">>> row", row)
    if contained_name_with_colname_rowname == "列名" or contained_name_with_colname_rowname == "都有":
        temp.insert(0, colnames)
   

    # # result_str = '\n'.join(['\t'.join(str(row)) for row in temp]) + '\n'
    # # string = '\n'.join(['\t'.join([str(x) for x in row]) for row in temp])
    string = '\n'.join(['\t'.join([str(x) if x is not None else "" for x in row])  
                     for row in temp])
    # pd.DataFrame(string, columns=colnames)
    # return dict(
    #     content = string,
    #     type="table",
    #     name="归一化后的表格"
    # )
    return 



if __name__ == "__main__":
    # 1. 首先判断data是否是空值
    # 读取csv文件 
    filepath = f'C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/dynamic_raincloud_chart_inputFile_with_multiple_columns.txt'
    filepath = f'C:/Users/Cherry/Desktop/setNA/data_washing_cleaned_input_file.txt'
    filepath = f'D:/微科盟工作/setNA/data_washing_cleaned_input_file.txt'
    # filepath = f'C:/Users/Cherry/Desktop/setNA/data_washing_cleaned_input_file2.txt'

    # 指定第一列作为索引
    # df = pd.read_table(filepath, sep = "\t", index_col = 0, header = 0)
    normalization_or_standardizatation(filepath,
                contained_name_with_colname_rowname ="都有",
                parametric_method="0",
                na_type="空值",
                na_value="",
                missing_value_threshold = 0)
    # batch_effect_rectification2('C:/Users/Cherry/Downloads/dynamic_grid_heatmap_with_mantel_test_env_file (3).txt',
    #         # "C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/",
    #         contained_name_with_colname_rowname ="都有",
    #         parametric_method="min-max")
    # MinFilledGlobalImputer().transform([['1', '', '']])