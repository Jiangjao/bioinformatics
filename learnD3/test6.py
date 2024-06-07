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
                min_value_in_row = min(row)
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = min_value_in_row


        return flag_mat



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


class AvgFilledByLineImputer(Normalization):

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
            if 2:
                row = [Decimal(x) for x in data_input[row_index] if is_number(x)]
                flag_value_in_row = data_mean
            for v in range(0, cols_length):
                # if min_value_in_row in data:
                if isinstance(flag_mat[row_index][v], float):
                    pass
                elif str(flag_mat[row_index][v]).strip() == str(na_value):
                    flag_mat[row_index][v] = flag_value_in_row


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
        'min': min,
        'max':max,
        'sum': statistics.median_low ,
        'colMax': MaxFilledByLineImputer,
        'colAvg': AvgFilledByLineImputer,
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

def get_stastics(matrix, handleFunction, parametric_method, flag=1):
    
    # 转置矩阵
    transposed_matrix = list(map(list, zip(*matrix)))
    # transposed = list(map(list, zip(*data)))

    # 计算每行的最大值、最小值和总和
    row_stats = []
    value_indices = []
    # 注意这个flag 是指的是列名的index
    flag = 1
    for index in range(0, len(transposed_matrix)):
        row = transposed_matrix[index]
        row_values_original = [value.strip() for value in row]
        row_values = [value for value in row_values_original if value]  # 去除空字符串
        row_values = [float(value) for value in row_values if is_number(value)]  # 转换为整数（如果适用）
        if len(row_values) == 0:
            continue
        row_stats.append({
            'Max': max(row_values),
            'Min': min(row_values),
            'Sum': sum(row_values),
            'median': statistics.median_low(row_values)
        })

        # 选中指定的列
        if index == flag:
            if parametric_method == "min":
                test_min_value = get_min_max_value(row_values, min)
                value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]
            elif parametric_method == "max":
                test_min_value = get_min_max_value(row_values, max)
                value_indices = [i for  i in range(0, len(row_values)) if row_values[i] == test_min_value]
            # index_row = row_values.index(test_min_value)
            # [].
            elif parametric_method == "sum":
                value_indices = [i for  i in range(0, len(row_values))]
            break

    # target_row = transform_nested_list([row])
    transposed_target_row = []
    for i in value_indices:
        transposed_target_row.append(matrix[i])
    # transposed_target_row = matrix[index_row]

    # 打印每行的统计信息
    for i, stats in enumerate(row_stats):
        print(f"Row {i+1}: {stats}")

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
    if na_value == None:
        na_value = na_format

    
    if na_value == "空值":
        # TODO:xiaojiao ，需要添加空格的校验
        na_value = ""
    
    counts = defaultdict(list)
    # 5-6. 计算/移除缺失率高行列
    # 参数判断
    if not isinstance(input_file, str):
        raise ValueError("输入文件不是字符串")
    if not isinstance(contained_name_with_colname_rowname, str):
        raise ValueError("contained_name_with_colname_rowname 不是字符串")
    if not isinstance(parametric_method, str):
        raise ValueError("parametric_method 不是字符串")
    
    choices = ["行名", "列名", "都有", "都没有"]
    parametric_method_choices = ['min', 'max', 'sum', 'colMin', 'colAvg', 'colMax', 'rowMin', 'rowAvg', 'rowMedian']

    if contained_name_with_colname_rowname not in choices:
        raise ValueError("contained_name_with_colname_rowname 参数错误")
    if parametric_method not in parametric_method_choices:
        raise ValueError("parametric_method 参数错误")


    # 将表格字符串转换为列表形式
    data = [line.split('\t') for line in input_file.split('\n') if line]

    # 拆分包含逗号分隔的字符串
    data = split_data_by_separator(data, ",")
    
    # data = new_rows
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

    duplicate_rownames_list

    counts = handle_duplicates_2_defaultdict(data, duplicate_rownames_list, rownames)
    # for duplicate_element_index in duplicate_rownames_list:
    #     duplicate_each_row = [rownames[duplicate_element_index]]
    #     each_element = data[duplicate_element_index]
    #     duplicate_each_row.extend(each_element)
    #     each_rowname =  str(rownames[duplicate_element_index]).strip()
    #     # 嵌套list
    #     counts[each_rowname].append(duplicate_each_row)

    row = []
    result_without_header = []

    
    # 原始数据去除这个
    data = filter_orginal_data(data, duplicate_rownames_list)
    new_rownames = filter_orginal_data(rownames, duplicate_rownames_list)

    temp2 = move_rownames_to_first_position(data, new_rownames)
    # 更新原始数据data

    # 4. 计算统计指标
    # 4.1 计算每行的最大值、最小值和总和
    # 4.2 选中指定的列
    for key, samples in counts.items():
        # handle samples
        # for sample, count in samples.items():
        for container in get_stastics(samples, get_min_max_value, parametric_method, flag=1):
            result_without_header.append(container)
    # TODO:xiaojiao
    if parametric_method == "sum":

        counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        # 计算每列的总和

        for line in result_without_header:
            values = line
            gene = values[0].strip()
            for i, value in enumerate(values[1:]):
                sample = colnames[i + 1]
                if is_number(value):
                    # counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                    counts.setdefault(gene, {})[sample] =  counts[gene].get(sample, 0) + float(value)
        nested_list = []

        # index = 0
        for gene, samples in counts.items():
            row = [gene]
            for sample, count in samples.items():

                row.append(count)
            nested_list.append(row)
        result_without_header = nested_list
        print("summary here>>>")
    counts
    result_without_header
    counts

    # 获得新行列数
    # 2.4 产生标记矩阵
    # 获取行列数

    # 3. 对缺失值进行标记

    temp = result_without_header
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
    normalization_or_standardizatation(filepath,
                contained_name_with_colname_rowname ="都有",
                parametric_method="sum",
                category_column_name="1",
                na_format="自定义",
                na_value="None")
