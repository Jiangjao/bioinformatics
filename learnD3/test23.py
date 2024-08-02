# !/usr/bin/python3
# encoding: utf-8
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import to_tree, ClusterNode, dendrogram
from typing import Dict, Tuple, List, Union, Optional
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from jinja2 import Environment, FileSystemLoader
# from task.core.decorators import register
import json
import functools #引入functools包

import functools
import json
import sys
from collections import deque
from scipy.cluster.hierarchy import ClusterNode
sys.setrecursionlimit(3000)

# https://zhuanlan.zhihu.com/p/90757416
# python——浅谈递归优化问题
# @listToTuple
HashDict = type('HashDict', (dict,), {'__hash__': lambda self: hash(json_hash(self))})
HashList = type('HashList', (list,), {'__hash__': lambda self: hash(json_hash(self))})
HashSet = type('HashSet', (set,), {'__hash__': lambda self: hash(json_hash(self))})
hashClusterNode = type('ClusterNode', (ClusterNode,), {
	'__hash__': lambda self: hash(json_hash(self)),
	'__eq__': lambda self, other: (isinstance(other, ClusterNode) and
								   self.id == other.id and
								   self.dist == other.dist and
								   self.left == other.left and
								   self.right == other.right)
})

def to_hash_object(obj, ):
	if isinstance(obj, dict):
		return HashDict(obj)
	elif isinstance(obj, list):
		return HashList(obj)
	elif isinstance(obj, set):
		return HashSet(obj)
	elif isinstance(obj, ClusterNode):
		return hashClusterNode(obj)
	return obj

def json_hash(obj):
    if isinstance(obj, HashableClusterNode):
        return hash((obj.id, obj.dist, obj.count, obj.left, obj.right))
    return to_hash_object(obj)
    # return hash(json.dumps(obj, sort_keys=True))

class HashableClusterNode:
    def __init__(self, id, dist, count, left=None, right=None):
        self.id = id
        self.dist = dist
        self.count = count
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __hash__(self):
        return json_hash(self)
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self.id == other.id and 
                    self.dist == other.dist and 
                    self.left == other.left and 
                    self.right == other.right)
        return False

# @functools.lru_cache(maxsize=128, typed=False)
def _scipy_tree_to_newick_list(root_node, parent_dist, leaf_names):
	"""Construct Newick tree from SciPy hierarchical clustering ClusterNode using stack.

	Args:
		root_node (scipy.cluster.hierarchy.ClusterNode): Root node is output of scipy.cluster.hierarchy.to_tree from hierarchical clustering linkage matrix
		parent_dist (float): Distance of parent node of `root_node`
		leaf_names (list of string): Leaf node names

	Returns:
		str: Newick format string
	"""
	if root_node is None:
		return []  # 如果节点为空，则返回空列表

	stack = [(root_node, root_node.dist, False)]  # 初始化栈，包含根节点、其距离和访问标志
	newick = []  # 初始化存储Newick字符串组件的列表

	while stack:
		current_node, current_dist, visited = stack.pop()  # 弹出栈顶元素

		if current_node.is_leaf():
			# 如果当前节点是叶节点，添加其名称和距离到newick列表
			newick.append(f'{leaf_names[current_node.id]}:{current_dist - current_node.dist}')
		else:
			if visited:
				# 如果当前节点已被访问过，添加Newick字符串的闭合部分
				if len(newick) > 0:
					newick.append(f'):{current_dist - current_node.dist}')
				else:
					newick.append(');')
			else:
				# 如果当前节点未被访问过，处理其子节点
				stack.append((current_node, current_dist, True))  # 重新压栈当前节点并设置访问标志为True
				if current_node.get_right() is not None:
					stack.append((current_node.get_right(), current_node.dist, False))  # 压入右子节点
					newick.append(',')  # 添加逗号以分隔兄弟节点
				if current_node.get_left() is not None:
					stack.append((current_node.get_left(), current_node.dist, False))  # 压入左子节点
					newick.append('(')  # 添加左括号以开始子节点列表
	return newick[::-1]  # 反转newick列表以获得正确顺序并返回

def to_newick(node, parentdist, leaf_names):
    """将SciPy层次聚类ClusterNode转换为Newick格式字符串

    参数:
        node (scipy.cluster.hierarchy.ClusterNode): 从层次聚类连接矩阵输出的根节点
        parentdist (float): `node`的父节点的距离
        leaf_names (list of string): 叶节点的名称

    返回:
        (string): Newick格式的字符串
    """
    # def convert_to_hashable(node):
    #     """递归转换 ClusterNode 为 HashableClusterNode"""
    #     if node is None:
    #         return None
    #     return HashableClusterNode(
    #         node.id, 
    #         node.dist, 
    #         node.count, 
    #         convert_to_hashable(node.left), 
    #         convert_to_hashable(node.right)
    #     )

    # # 将输入的ClusterNode转换为可哈希的ClusterNode
    # hash_node = convert_to_hashable(node)
    # 获取Newick字符串列表
    newick_list = _scipy_tree_to_newick_list(node, node.dist, leaf_names)
    # 连接并返回Newick字符串
    return ''.join(newick_list)
    
    # 将输入的ClusterNode转换为可哈希的ClusterNode
    hash_node = convert_to_hashable(node)
    # 获取Newick字符串列表
    newick_list = _scipy_tree_to_newick_list(hash_node, parentdist, leaf_names)
    # 连接并返回Newick字符串
    return ''.join(newick_list)



#  Example usage:
import pandas as pd
from scipy.cluster.hierarchy import linkage

# Sample data
# data = {
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# }
# df = pd.DataFrame(data)

# # Normalize the dataframe
# # normalized_df = (df - df.mean()) / df.std()
# scaler = StandardScaler()
# normalized_df = scaler.fit_transform(df)
# # Generate the linkage matrix
# Z = linkage(normalized_df, method='weighted', metric='euclidean')

# # Generate the clustering tree
# T = to_tree(Z, rd=False)

# # Define the leaf names
# leaf_names = df.index.tolist()

# Get the Newick format string
# newick_str = to_newick(T, leaf_names)
# print(newick_str)


def to_newick(node, parentdist, leaf_names):
    """将SciPy层次聚类ClusterNode转换为Newick格式字符串

    参数:
        node (scipy.cluster.hierarchy.ClusterNode): 从层次聚类连接矩阵输出的根节点
        parentdist (float): `node`的父节点的距离
        leaf_names (list of string): 叶节点的名称

    返回:
        (string): Newick格式的字符串
    """
    # 获取Newick字符串列表
    newick_list = _scipy_tree_to_newick_list(node, node.dist, leaf_names)
    # 连接并返回Newick字符串
    return "".join(newick_list[::-1])
# Example usage:
import pandas as pd
from scipy.cluster.hierarchy import linkage

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
# df = pd.DataFrame(data)

# # Normalize the dataframe
# # normalized_df = (df - df.mean()) / df.std()
# # 将归一化后的数据转换为DataFrame
# scaler = StandardScaler()
# normalized_data = scaler.fit_transform(df)
# min_max_normalization = 0
# normalized_df = pd.DataFrame(normalized_data, index=df.index, columns=df.columns)

# # Generate the linkage matrix
# Z = linkage(normalized_df, method='weighted', metric='euclidean')

# # Generate the clustering tree
# T = to_tree(Z, rd=False)


# ((1:2.1213203435596424,0:2.1213203435596424):1.0606601717798214,2:3.181980515339464);
# ((1:2.1213203435596424,0:2.1213203435596424):1.0606601717798214,2:3.181980515339464);
# (2:3.181980515339464,(0:2.1213203435596424,1:2.1213203435596424),:1.0606601717798214):0.0;
# :0.0(Sample3:2.598076211353316,(Sample1:1.7320508075688772,Sample2:1.7320508075688772),:0.8660254037844388);

heatmap_file = "C:/Users/Cherry/Downloads/circle_heatmap_chart_heatmap_file.txt"
# heatmap_file = "C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/heatmap2.txt"
# heatmap_file = "/var/www/cloud_workdir/534/circle_heatmap_chartMkQ66U7Y8NY7WkNXDPVkSA/data/heatmap_file.txt"
	# circle_heatmap_chart("/var/www/cloud_workdir/10917/circle_heatmap_chartDDr8pADBaAxgJahgSPQypL/data/heatmap_file.txt",
# heatmap_file = "/var/www/cloud_workdir/10917/circle_heatmap_chartDDr8pADBaAxgJahgSPQypL/data/heatmap_file.txt"
df = pd.read_table(heatmap_file, index_col=0, header=0)
# df = pd.read_table(data, index_col=0, header=0)
# df = pd.DataFrame(data)
f = df.apply(pd.to_numeric, errors='coerce')
# 2024/07/04
# 去除空值
df = df.dropna(how='all') # 去除全部转换失败的行
# 2024、06、03 去除非数值的列
# 保留数值类型列
for df_column in df.columns.to_list():
    df[df_column] = pd.to_numeric(df[df_column], errors='coerce')
# print(df)
# 将无法转换为数值的值替换为 NaN
df = df.apply(pd.to_numeric, errors='coerce')
# 去除NA值的列 2024、06、03
df.dropna(axis=1, how='any', inplace=True)
# df.dropna(axis=0, how='any', inplace=True)

# 创建一个空的DataFrame用于存储归一化后的数据
normalized_df = pd.DataFrame()
min_max_normalization = 1

# 检查 DataFrame 中的列是否都是数值型数据
if not all(df.dtypes.apply(pd.api.types.is_numeric_dtype)):
    raise ValueError("All columns in DataFrame must be numeric")
# df = pd.DataFrame(data)

# Normalize the dataframe
# normalized_df = (df - df.mean()) / df.std()
# 将归一化后的数据转换为DataFrame
scaler = StandardScaler()
normalized_data = scaler.fit_transform(df)
min_max_normalization = 0
normalized_df = pd.DataFrame(normalized_data, index=df.index, columns=df.columns)

# 获取行名
row_names = df.index.tolist()
# Generate the linkage matrix
# scaler = StandardScaler()
# normalized_df = scaler.fit_transform(data)
# 获取行名
# row_names = list([0, 1, 2])
row_names = df.index
# 进行层次聚类
Z = hierarchy.linkage(normalized_df, method='weighted', metric='euclidean')
T = to_tree(Z, rd=False)


# Define the leaf names
leaf_names = df.index.tolist()

# Get the Newick format string
newick_str = to_newick(T, T.dist, leaf_names)
# print(newick_str)

newick_str = newick_str.rstrip('):0.0') + ';'
newick_str = newick_str.lstrip(',')
print(f"Newick format tree written to output_tree.newick:\n{newick_str}")

# 获取行名
row_names = df.index.tolist()
nwk = newick_str
numSegments = len(list(row_names))
# print("row_names", list(row_names))
# 转换为所需的格式
output = []
for index, row in normalized_df.T.iterrows():
    data = {
        "group": row.values.tolist(),
        "id": index
    }
    output.append(data)
print(output)
numSegments = len(list(row_names))
print(numSegments)