# !/usr/bin/python3
# --- encoding: utf-8 ---
import statistics
import math
from abc import ABC, abstractmethod
import random
from decimal import Decimal, getcontext
from functools import partial
from collections import defaultdict
from types import FunctionType
import copy
import re
from collections import UserString

import os
import hashlib


# 设置精度
getcontext().prec = 64

def transform_nested_list(data):
    """
    交叉转置二维嵌套列表

    Args:
        data: 嵌套列表

    Returns:list
    转置后的列表
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


class Normalization(ABC):
    @abstractmethod
    def transform(self, data):
        pass

    def get_stastics(self, matrix, parametric_method, colnames, flag):
        pass

# #  MinMaxNormalizer类
# # 0 - 1 归一化
class MinFilledGlobalImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_min = data.data_min

        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0])
        results = [None] * len_df1
        index  = 0
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
                elif str(flag_mat[row_index][v]).strip() == str(na_value).strip():
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
        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min
        # TODO: xiaojiao, 需要重写这个算法
        
        len_df1 = len(data_input)
        cols_length = len(data_input[0])
        results = [None] * len_df1
        index  = 0
        colnames = None

        # 重写这个
        # 3. 对缺失值进行标记
        for row_index in range(0, len_df1):
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


class MinFilledByLineImputer(Normalization):

    def transform(self, result_without_header, colnames, id_cols_index, random_string):

        counts = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))

        for line in result_without_header:
            values = line
            gene = values[0].strip()

            # 空白直接跳过, 暂时舍弃
            if gene == None:
                continue
            if len(gene) == 0:
                continue
            # is_number_flag = False

            for i, value in enumerate(values[1:]):
                sample = colnames[i + 1]
                is_number_flag = is_number(value)
                if len(id_cols_index) == 0:
                    
                    if is_number_flag:
                        counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    else:
                        # 添加 同类别分行
                        # value_pre = counts[gene].get(sample, "")
                        # if value not in value_pre.split(sep):
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)
                            # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                            # counts[gene][sample] = f"{value_pre}{sep}{value}"
                else:
                    # 指定列不用数学运算，字符串拼接就行
                    if i in id_cols_index:
                        # value_pre = counts[gene].get(sample, "")
                        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)
                    elif is_number_flag:
                        counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    else:
                        # 添加 同类别分行
                        # value_pre = counts[gene].get(sample, "")
                        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)

        result_without_header = generate_result_with_sum(counts, random_string)
        print("summary here>>>")

        return result_without_header

    def get_stastics(self, matrix, parametric_method, colnames, flag):
        # 转置矩阵
        transposed_matrix = list(map(list, zip(*matrix)))

        value_indices = []

        # 是否获取第一个数值列？
        get_index = lambda matrix: next((i for i, x in enumerate(matrix) if is_number(x)), None)
        index = get_index(matrix[0])

        flag = 1

        transposed_matrix_length = len(transposed_matrix)
        for index in range(0, transposed_matrix_length):
            row = transposed_matrix[index]
            row_values_original = [value.strip() for value in row]
            row_values = [value for value in row_values_original if value]  # 去除空字符串

            if 1:
                row_values = [value for value in row_values_original if value]  # 去除空字符串
                row_values = [float(value) for value in row_values if is_number(value)]  # 转换为整数（如果适用）
                if len(row_values) == 0:
                    continue

                # 选中指定的列
                # TODO:Xiaojiao, 需要修复这里的一行2024、04、30
                if index == flag:
                    if parametric_method == "min":
                        test_min_value = get_min_max_value(row_values, min)
                        value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]

                    elif parametric_method == "max":
                        test_min_value = get_min_max_value(row_values, max)
                        value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]
                    break

        if 1:
            # target_row = transform_nested_list([row])
            transposed_target_row = []
            for i in value_indices:
                transposed_target_row.append(matrix[i])

            return transposed_target_row

class MaxFilledByLineImputer(Normalization):

    def transform(self, data):
        # 注意传入的是一个data对象
        data_input = data.data
        flag_mat = transform_nested_list(data.data_flag)
        na_value = data.na_value
        data_max = data.data_max
        data_min = data.data_min

        # 注意传入的是一个data对象
        data_input = data.data
        data_max = data.data_max
        data_min = data.data_min
        data_mean = data.data_mean
        
        data_interval = data_max - data_min

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

    def get_stastics(self, matrix, parametric_method, colnames, flag):
        # 转置矩阵
        transposed_matrix = list(map(list, zip(*matrix)))

        value_indices = []

        # 是否获取第一个数值列？
        get_index = lambda matrix: next((i for i, x in enumerate(matrix) if is_number(x)), None)
        index = get_index(matrix[0])

        flag = 1

        transposed_matrix_length = len(transposed_matrix)
        for index in range(0, transposed_matrix_length):
            row = transposed_matrix[index]
            row_values_original = [value.strip() for value in row]
            row_values = [value for value in row_values_original if value]  # 去除空字符串

            if 1:
                row_values = [value for value in row_values_original if value]  # 去除空字符串
                row_values = [float(value) for value in row_values if is_number(value)]  # 转换为整数（如果适用）
                if len(row_values) == 0:
                    continue

                # 选中指定的列
                # TODO:Xiaojiao, 需要修复这里的一行2024、04、30
                if index == flag:
                    if parametric_method == "min":
                        test_min_value = get_min_max_value(row_values, min)
                        value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]

                    elif parametric_method == "max":
                        test_min_value = get_min_max_value(row_values, max)
                        value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]
                    break

        if 1:
            # target_row = transform_nested_list([row])
            transposed_target_row = []
            for i in value_indices:
                transposed_target_row.append(matrix[i])

            return transposed_target_row

class SumFilledByLineImputer(Normalization):

    def transform(self, result_without_header, colnames, id_cols_index, random_string):

        counts = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))

        for line in result_without_header:
            values = line
            gene = values[0].strip()

            # 空白直接跳过, 暂时舍弃
            if gene == None:
                continue
            if len(gene) == 0:
                continue
            for i, value in enumerate(values[1:]):
                sample = colnames[i + 1]
                is_number_flag = is_number(value)
                if len(id_cols_index) == 0:
                    if is_number_flag:
                        counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    else:
                        # 添加 同类别分行
                        # value_pre = counts[gene].get(sample, "")
                        # if value not in value_pre.split(sep):
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)
                            # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                            # counts[gene][sample] = f"{value_pre}{sep}{value}"
                else:
                    # 指定列不用数学运算，字符串拼接就行
                    if i in id_cols_index:
                        # value_pre = counts[gene].get(sample, "")
                        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                        # counts[gene][sample] = counts[gene].get(sample, "") + str(value)
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)
                    elif is_number_flag:
                        counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    else:
                        # 添加 同类别分行
                        # value_pre = counts[gene].get(sample, "")
                        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)

        result_without_header = generate_result_with_sum(counts, random_string)
        print("summary here>>>")

        return result_without_header
   
    def get_stastics(self, matrix, parametric_method, colnames, flag):
        # 转置矩阵
        transposed_matrix = list(map(list, zip(*matrix)))
        transposed_target_row = []
        value_indices = []

        get_index = lambda matrix: next((i for i, x in enumerate(matrix) if is_number(x)), None)
        index = get_index(matrix[0])

        flag = 1
        colnames_without_first = colnames
        id_cols_index = [i for i, col in enumerate(colnames_without_first)
                            if re.search(r'\bid$', col, re.IGNORECASE)]
        transposed_matrix_length = len(transposed_matrix)
        for index in range(0, transposed_matrix_length):
            row = transposed_matrix[index]
            row_values_original = [value.strip() for value in row]
            row_values = [value for value in row_values_original if value]  # 去除空字符串
            row_values = [float(value) for value in row_values if is_number(value)]  # 转换为整数（如果适用）
            if len(row_values) == 0:
                continue

            if parametric_method == "sum":
                value_indices = [i for  i in range(0, len(row_values))]

        for i in value_indices:
            transposed_target_row.append(matrix[i])

        return transposed_target_row


class AvgFilledGlobalImputer(Normalization):

    def transform(self, result_without_header, colnames, id_cols_index, random_string):

        counts = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))

        for line in result_without_header:
            values = line
            gene = values[0].strip()

            # 空白直接跳过, 暂时舍弃
            if gene == None:
                continue
            if len(gene) == 0:
                continue
            # is_number_flag = False

            for i, value in enumerate(values[1:]):
                sample = colnames[i + 1]
                is_number_flag = is_number(value)
                if len(id_cols_index) == 0:
                    
                    if is_number_flag:
                        # row_length
                        counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    else:
                        # 添加 同类别分行
                        # value_pre = counts[gene].get(sample, "")
                        # if value not in value_pre.split(sep):
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)
                            # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                            # counts[gene][sample] = f"{value_pre}{sep}{value}"
                else:
                    # 指定列不用数学运算，字符串拼接就行
                    if i in id_cols_index:
                        # value_pre = counts[gene].get(sample, "")
                        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                        value = str(value)
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)
                    elif is_number_flag:
                        counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    else:
                        # 添加 同类别分行
                        # value_pre = counts[gene].get(sample, "")
                        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                        process_value_by_each_line_with_substring(counts, gene, sample, value, random_string)

        result_without_header = generate_result_with_sum(counts, random_string)
        print("summary here>>>")

        return result_without_header

    
    def get_stastics(self, matrix, parametric_method, colnames, flag):

        # 转置矩阵
        transposed_matrix = list(map(list, zip(*matrix)))
        # transposed = list(map(list, zip(*data)))

        # 计算每行的最大值、最小值和总和
        row_stats = []
        value_indices = []
        get_index = lambda matrix: next((i for i, x in enumerate(matrix) if is_number(x)), None)
        index = get_index(matrix[0])

        flag = 1
        colnames_without_first = colnames
        id_cols_index = [i for i, col in enumerate(colnames_without_first)
                            if re.search(r'\bid$', col, re.IGNORECASE)]
        transposed_matrix_length = len(transposed_matrix)
        bracket = [None] * transposed_matrix_length
        for index in range(0, transposed_matrix_length):
            row = transposed_matrix[index]
            row_values_original = [value.strip() for value in row]
            row_values = [value for value in row_values_original if value]  # 去除空字符串

            if parametric_method == "avg":
                # pass
                is_list_full_number = all([is_number(i) for i in row])
                # for each_element in enumerate(row):
                if index in id_cols_index:
                    element_average = ",".join(set(row_values))
                elif is_list_full_number:
                    row_values = [float(value) for value in row_values_original if is_number(value)]  # 转换为整数（如果适用）
                    element_average = statistics.mean(row_values)
                else:
                    element_average = ",".join(set(row_values))
                bracket[index] = element_average
        transposed_target_row = []
        if parametric_method == "avg":
            transposed_target_row.append(bracket)
            return [bracket]

# # 5. center 中心值归一化
class CenterNormalizer(Normalization):
    
    def transform(self, data):
        # mean = np.mean(data)
        data_input = data.data
        data_mean = data.data_mean
        data_std = data.data_std
        
        len_df1 = len(data_input)
        cols = len(data_input[0])
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
       
        means = [x for x in means if x is not None]
        return means
        return (data - mean)


# 工厂
# 其他归一化类

class NormalizationFactory:

    normalizer_map = {
        'min': MinFilledByLineImputer,
        'max':MinFilledByLineImputer,
        'sum': SumFilledByLineImputer,
        'colMax': MaxFilledByLineImputer,
        # 'colAvg': AvgFilledByLineImputer,
        'avg': AvgFilledGlobalImputer,
        'center': CenterNormalizer
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
        # 如果是数字
        float(s)
        return True
    except ValueError:
        pass
 
    return False

def find_duplicates_with_index(lst):
    """
    param: lst(list)
    
    return dict
    """
    duplicates = defaultdict(list)
    seen = set()

    for i, item in enumerate(lst):
        item = item.strip()
        duplicates[item].append(i)
        if item in seen:
            # if item in duplicates:
            #     duplicates[item].append(i)
            # else:
            #     duplicates[item].append(i)
            pass
                # duplicates[item] = [i]
        else:
            seen.add(item)

    return {key: value for key, value in duplicates.items() if len(value) > 1}

def get_min_max_value(listt, function):
    test_value = function(listt)
    return test_value

def get_stastics(matrix, handleFunction, parametric_method, colnames, flag=1):

    # 转置矩阵
    transposed_matrix = list(map(list, zip(*matrix)))

    value_indices = []

    # 是否获取第一个数值列？
    get_index = lambda matrix: next((i for i, x in enumerate(matrix) if is_number(x)), None)
    index = get_index(matrix[0])

    flag = 1
    colnames_without_first = colnames
    id_cols_index = [i for i, col in enumerate(colnames_without_first)
                        if re.search(r'\bid$', col, re.IGNORECASE)]
    transposed_matrix_length = len(transposed_matrix)
    bracket = [None] * transposed_matrix_length
    for index in range(0, transposed_matrix_length):
        row = transposed_matrix[index]
        row_values_original = [value.strip() for value in row]
        row_values = [value for value in row_values_original if value]  # 去除空字符串

        if parametric_method == "avg":
            # pass
            is_list_full_number = all([is_number(i) for i in row])
            # for each_element in enumerate(row):
            if index in id_cols_index:
                element_average = ",".join(set(row_values))
            elif is_list_full_number:
                row_values = [float(value) for value in row_values_original if is_number(value)]  # 转换为整数（如果适用）
                element_average = statistics.mean(row_values)
            else:
                element_average = ",".join(set(row_values))
            bracket[index] = element_average
        else:
            row_values = [value for value in row_values_original if value]  # 去除空字符串
            row_values = [float(value) for value in row_values if is_number(value)]  # 转换为整数（如果适用）
            if len(row_values) == 0:
                continue

            if parametric_method == "sum":
                value_indices = [i for  i in range(0, len(row_values))]
            if parametric_method == "avg":
                value_indices = [i for  i in range(0, len(row_values))]
            # 选中指定的列
            # TODO:Xiaojiao, 需要修复这里的一行2024、04、30
            if index == flag:
                if parametric_method == "min":
                    test_min_value = get_min_max_value(row_values, min)
                    value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]

                elif parametric_method == "max":
                    test_min_value = get_min_max_value(row_values, max)
                    value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]
                break

    if parametric_method == "avg":
        return [bracket]
    else:
        # target_row = transform_nested_list([row])
        transposed_target_row = []
        for i in value_indices:
            transposed_target_row.append(matrix[i])

        return transposed_target_row

def split_data_by_separator(data, separator):
    """
    Split data based on a specified separator.

    Args:
    - data: A list containing the data, where each element represents a row of data.
    - separator: The separator used to split the string in the first element.

    Returns:
    A list of split data.

    Example usage:
    split_rows = split_data_by_separator(data, ',')
    for row in split_rows:
        print(row)
    """
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string")
        
    if not re.match(r'\s*', separator):
        raise ValueError("Separator must be a valid separator")
    # 切割数据
    new_rows = []

    # 需要分割第一列
    for i, row in enumerate(data):
        first_element = row[0]
        remaining_elements = row[1:]
        # if i == 0 and separator in first_element:
        split_values = first_element.split(separator)
        # remove the space for each element
        # TODO:xiaojiao, 去除字符串中的空格, 和上面是否需要统一
        # 如果sepeator 是空格会不会报错
        split_values = [x.strip() for x in split_values]
        for value in split_values:
            new_row = [value] + remaining_elements
            new_rows.append(new_row)

    return new_rows

def swap_columns(matrix, col1, col2):
    """
    Swap two columns in a matrix.

    This function takes a matrix and swaps the positions of the two 
    columns specified by their indices.

    Args:
        matrix: A 2D list representing the matrix.
        col1: Index of the first column to swap. 
        col2: Index of the second column to swap.

    Returns:
        The input matrix with the columns at col1 and col2 swapped.

    Examples:
        >>> matrix = [[1,2,3],  
                    [4,5,6]]
                    
        >>> swapped = swap_columns(matrix, 0, 1)
        
        >>> print(swapped)
        [[2, 1, 3],
        [5, 4, 6]]
    """

    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]


def filter_orginal_data(data, duplicate_rownames_list):
    # import copy
    data = copy.deepcopy(data)
    # 原始数据去除这个
    for i in duplicate_rownames_list:
        data[i] = None
    
    # 去除
    data = [line for line in data if line != None]
    return data

def move_rownames_to_first_position(data, rownames):
    """
    Move each element of rownames to the first position of each corresponding row in data.

    Args:
    - data: A list containing the data.
    - rownames: A list containing the row names.

    Returns:
    The modified data with row names moved to the first position.

    Example usage:
    modified_data = move_rownames_to_first_position(data, rownames)
    """

    # Check if the lengths of data and rownames match
    if len(data) != len(rownames):
        raise ValueError("The lengths of data and rownames do not match.")

    # Move row names to the first position of each row in data
    modified_data = []
    for i in range(len(data)):
        modified_row = [rownames[i]] + data[i]
        modified_data.append(modified_row)

    return modified_data

def handle_duplicates_2_defaultdict(data, duplicate_rownames_list, rownames):
    """
    处理重复数据,统计重复行
    
    将数据中重复的行合并统计到counts中

    参数:
    - data: 原始数据列表
    - counts: 重复数据统计结果 defaultdict
    - duplicate_rownames_list: 重复索引列表 
    - rownames: 行名列表
        
    过程:
    1. 遍历重复索引列表
    2. 根据索引提取重复行数据
    3. 构建统计行,包括行名和值
    4. 将统计行添加到counts中

    返回:
    处理后counts,作为统计结果
    """
    # 处理重复数据
    counts = defaultdict(list)

    for duplicate_element_index in duplicate_rownames_list:
        duplicate_each_row = [rownames[duplicate_element_index]]
        each_element = data[duplicate_element_index]
        duplicate_each_row.extend(each_element)
        each_rowname =  str(rownames[duplicate_element_index]).strip()
        # 嵌套list
        counts[each_rowname].append(duplicate_each_row)
    return counts

def find_colnames_with_id():
    pass

def update_value_tool(counts, gene, sample, value, sep=" "):
    value_pre = counts[gene].get(sample, "")
    counts[gene][sample] = f"{value_pre}{sep}{value}"

def generate_result_with_sum(counts, random_string):
    nested_list = []
    for gene, samples in counts.items():
        row = [gene]
        for sample, count in samples.items():
            if not is_number(count):
                count = count.replace(random_string,"")
            row.append(count)
        nested_list.append(row)
    return nested_list

def process_value_by_each_line_with_substring(counts, gene, sample, value, random_string):
    """处理每行数据中的值,如果值中包含分隔子串则跳过,否则添加分隔符拼接
        
    Args:
        counts (dict): 统计计数字典
        gene (str): 基因
        sample (str): 样本
        value (str): 值
        random_string (str): 分隔符
        
    This function processes the value in each line of data. 
    It splits the previous value by the random_string separator,
    and checks if the current value is contained in any substring.
    If contained, it skips. Otherwise, it concatenates the previous
    value, separator and current value.
    """
    sep = " ,"
    value_pre = counts[gene].get(sample, "")
    if value != "":
        value = ",".join(set([i.strip() for i in value.split(",")]))
    # if value not in value_pre.split(sep):
    try:
        random_string = random_string + sep
        if value_pre == "":
            counts[gene][sample] = f"{value}"
            return
        for substring in value_pre.split(random_string):
            # 字母字符串长度相等
            if len(substring.strip()) == len(value.strip()):
                counts[gene][sample] = f"{value_pre}"
                return
            if value not in substring:
            # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
                counts[gene][sample] = f"{value_pre}{random_string}{value}"
            else:
                # 字母字符串包含
                if len(substring.strip()) == len(value.strip()):
                    # 基本上判定一致
                    counts[gene][sample] = f"{value_pre}"
                    pass
    except Exception as e:
        counts[gene][sample] = f"{value_pre}{random_string}{value}"
        # TODO:xiaojiao, 这里需要加上什么样的分隔符呢？
        # counts[gene][sample] = f"{value_pre}{value}"


class Tokenizer:

    def __init__(self):
        self.pattern = r"\w+"

    def split(self, text):
        return re.split(self.pattern, text)

    def tokenize(self, text):
        words = self.split(text)
        return words


def normalization_or_standardizatation(input_file, contained_name_with_colname_rowname, category_column_name, parametric_method, na_format, na_value):

    # 1. 设置字符串

    # 调试使用, debug
    if isinstance(input_file, str):
        with open(input_file) as f:
            input_file = f.read()
    # 2. 设定缺失值编码  
    # na_value = na_format
    # na_value = None
    if na_format == "自定义":
        na_value = na_value.strip()
    
    # local
    if na_value == None:
        na_value = na_format

    
    if na_value == "空值":
        # TODO:xiaojiao ，需要添加空格的校验
        na_value = " "
    
    counts = defaultdict(list)
    # 调用分词器
    tokenizer = Tokenizer()
    # 参数判断
    if not isinstance(input_file, str):
        raise ValueError("输入文件不是字符串")
    if not isinstance(contained_name_with_colname_rowname, str):
        raise ValueError("contained_name_with_colname_rowname 不是字符串")
    if not isinstance(parametric_method, str):
        raise ValueError("parametric_method 不是字符串")
    
    choices = ["行名", "列名", "都有", "都没有"]
    parametric_method_choices = ['min', 'max', 'sum', 'avg', 'colAvg', 'colMax', 'rowMin', 'rowAvg', 'rowMedian']

    if contained_name_with_colname_rowname not in choices:
        raise ValueError("contained_name_with_colname_rowname 参数错误")
    if parametric_method not in parametric_method_choices:
        raise ValueError("parametric_method 参数错误")


    # 将表格字符串转换为列表形式
    data = [line.split('\t') for line in input_file.split('\n') if line]

    # 列名
    colnames = data[0]
    category_column_name = str(category_column_name).strip()
    # category_column_name = "sample02"
    colnames = [str(x).strip() for x in colnames]
    groupindex = colnames.index(category_column_name)

    # 交换位置
    swap_columns(data, col1=0, col2=groupindex)
    # 拆分包含逗号分隔的字符串
    data = split_data_by_separator(data, na_value)

    # data = new_rows
    # TODO:xiaojiao, 去除字符串中的空格
    len_data = len(data)
    length_cols = len(data[0]) - 1
    rownames = [None] * len_data
    colnames = [None] * length_cols
    # colnames = data.pop(0)
    index = 0
    random_string = hashlib.md5(os.urandom(32)).hexdigest()

    # TODO:xiaojiao, 增加contained_name_with_colname_rowname与文件行列情况不对应的状态
    # 1. 都有
    if contained_name_with_colname_rowname == "都有":
        index = 0
        colnames = data.pop(0)
        for line in data:
            rownames[index] = line.pop(0)
            index += 1
    elif contained_name_with_colname_rowname == "行名":

        for line in data:
            rownames[index] = line.pop(0)
            index += 1

    elif contained_name_with_colname_rowname == "列名":
        colnames = data.pop(0)

    elif contained_name_with_colname_rowname == "都没有":

        index = 0

    # 判断是否是矩阵，不包含空值
    for row in data:
        if len(row) != length_cols:
            raise ValueError("数据格式错误, 包含空值, 请参考示例文件检查数据文件是否正确。")

    # 去除None
    rownames = [x for x in rownames if x is not None]

    # 2. 处理重复行 
    duplicate_rownames_dict =  find_duplicates_with_index(rownames)
    # 变成一维数组
    duplicate_rownames_list = []
    print(duplicate_rownames_dict)
    # 遍历 defaultdict 中的列表
    duplicate_rownames_list = [
        idx for value in duplicate_rownames_dict.values() for idx in value
    ]

    counts = handle_duplicates_2_defaultdict(data, duplicate_rownames_list, rownames)

    result_without_header = []

    
    # 原始数据去除这个
    data = filter_orginal_data(data, duplicate_rownames_list)
    new_rownames = filter_orginal_data(rownames, duplicate_rownames_list)

    category_column_name = str(category_column_name).strip()
    # category_column_name = "sample02"
    colnames = [str(x).strip() for x in colnames]
    # id_flag = re.IGNORECASE("\bid$")
    
    # 查询列名是否包含Id, 返回对应的index
    # 注意列名不能是纯数字
    colnames_without_first = colnames[1:]
    id_cols_index = [i for i, col in enumerate(colnames_without_first)
                        if re.search(r'\bid$', col, re.IGNORECASE)]

    groupindex = colnames.index(category_column_name)
    temp2 = move_rownames_to_first_position(data, new_rownames)
    # 更新原始数据data
    duplicate_element_in_string_remove = lambda string, separtor: [i.strip()
                                                         for i in set(string.split(","))]
    norm =  NormalizationFactory()
    norm = norm.get_normalizer("min")
    # temp0 = 
    # 4. 计算统计指标
    # 4.1 计算每行的最大值、最小值和总和
    # 4.2 选中指定的列
    for key, samples in counts.items():
        # handle samples
        # for sample, count in samples.items():
        for container in norm.get_stastics(samples, parametric_method, colnames, groupindex):
            # 去除第0个列名为空的
            if len(container[0]) == 0: continue
            # 每个列名去重
            result_without_header.append(container)
    # TODO:xiaojiao


    # norm.get_normalizer("sum")
    # result_without_header = norm.get_normalizer("sum").transform(result_without_header,
    #                                                              colnames, id_cols_index, random_string)
    
    # result_without_header = norm.get_normalizer("min").transform(result_without_header,
    #                                                              colnames, id_cols_index, random_string)
    result_without_header = norm.transform(result_without_header,
                                                                 colnames, id_cols_index, random_string)
    counts
    counts
    result_without_header

    # 获得新行列数
    # 2.4 产生标记矩阵
    # 获取行列数

    # 3. 对缺失值进行标记

    temp = result_without_header
    for i in temp:
        if len(i) == 21:
            pass
        else:
            print(i)
            print(len(i))
    # 将结果转换为制表符分隔的字符串
    colnames = [str(x) if x else "" for x in colnames]
    temp.insert(0, colnames)
    temp.extend(temp2)
    # if contained_name_with_colname_rowname == "行名" or contained_name_with_colname_rowname == "都有":
    #     index = 0
    #     for row in temp:
    #         row.insert(0, rownames[index]) 
    #         index += 1

    # if contained_name_with_colname_rowname == "列名" or contained_name_with_colname_rowname == "都有":
    #     temp.insert(0, colnames)

    string = '\n'.join(['\t'.join([str(x) if x is not None else "" for x in row])  
                     for row in temp])
    string = string.replace(random_string, "")
    print(string)
    return dict(
        content = string,
        type="table",
        name="归一化后的表格"
    )



if __name__ == "__main__":
    # 1. 首先判断data是否是空值
    # 读取csv文件 
    filepath = f'C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count_particle_duplicate.tsv'
    # 指定第一列作为索引
    # df = pd.read_table(filepath, sep = "\t", index_col = 0, header = 0)
    # normalization_or_standardizatation(filepath,
    #             contained_name_with_colname_rowname ="都有",
    #             parametric_method="sum",
    #             category_column_name="sample02",
    #             na_format="自定义",
    #             na_value="None")
    normalization_or_standardizatation(filepath,
            contained_name_with_colname_rowname ="都有",
            parametric_method="min",
            category_column_name="GO",
            na_format=",",
            na_value=None)
