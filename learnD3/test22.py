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
# import cache
import functools #引入functools包

#your cached function
# Generating Newick string output from hierarchical clustering of some cgMLST profiles
# source code from https://gist.github.com/peterk87/b203f62a71d7f4fb273139b219af5e81
# @listToTuple
# HashDict = type('HashDict', (dict,), {'__hash__': lambda self: hash(json_hash(self))})
# HashList = type('HashList', (list,), {'__hash__': lambda self: hash(json_hash(self))})
# HashSet = type('HashSet', (set,), {'__hash__': lambda self: hash(json_hash(self))})
# hashClusterNode = type('ClusterNode', (ClusterNode,), {
# 	'__hash__': lambda self: hash(json_hash(self)),
# 	'__eq__': lambda self, other: (isinstance(other, ClusterNode) and
# 								   self.id == other.id and
# 								   self.dist == other.dist and
# 								   self.left == other.left and
# 								   self.right == other.right)
# })

# def to_hash_object(obj, ):
# 	if isinstance(obj, dict):
# 		return HashDict(obj)
# 	elif isinstance(obj, list):
# 		return HashList(obj)
# 	elif isinstance(obj, set):
# 		return HashSet(obj)
# 	elif isinstance(obj, ClusterNode):
# 		return hashClusterNode(obj)
# 	return obj


# def lru_cache(*lru_args, **lru_kwargs):
# 	def wrapper_cache(func):
# 		func = functools.lru_cache(*lru_args, **lru_kwargs)(func)

# 		@functools.wraps(func)
# 		def wrapped_func(*args, **kwargs):
# 			return func(*map(to_hash_object, args), **{k: to_hash_object(v) for k, v in kwargs.items()})
# 		return wrapped_func
# 	return wrapper_cache

# 定义一个哈希函数，使用对象的属性
# def json_hash(obj):
#     if isinstance(obj, HashableClusterNode):
#         return hash((obj.id, obj.dist, obj.count, obj.left, obj.right))
#     return hash(json.dumps(obj, sort_keys=True))

# # 创建一个可以哈希的 ClusterNode 类
# class HashableClusterNode:
#     def __init__(self, id, dist, count, left=None, right=None):
#         self.id = id
#         self.dist = dist
#         self.count = count
#         self.left = left
#         self.right = right

#     def is_leaf(self):
#         return self.left is None and self.right is None

#     def get_left(self):
#         return self.left

#     def get_right(self):
#         return self.right

#     def __hash__(self):
#         return json_hash(self)
    
#     def __lt__(self, node):
#         if not isinstance(node, ClusterNode):
#             raise ValueError("Can't compare ClusterNode "
#                              "to type {}".format(type(node)))
#         return self.dist < node.dist

#     def __gt__(self, node):
#         if not isinstance(node, ClusterNode):
#             raise ValueError("Can't compare ClusterNode "
#                              "to type {}".format(type(node)))
#         return self.dist > node.dist

#     def __eq__(self, node):
#         if not isinstance(node, ClusterNode):
        #     raise ValueError("Can't compare ClusterNode "
        #                      "to type {}".format(type(node)))
        # return self.dist == node.dist

# 使用 functools.lru_cache 装饰器缓存函数结果
@functools.lru_cache(maxsize=128, typed=False)
def _scipy_tree_to_newick_list(node, newick, parentdist, leaf_names):
    """从SciPy层次聚类ClusterNode构建Newick树

    这是一个递归函数，用于从scipy.cluster.hierarchy.to_tree的输入构建Newick输出字符串，
    并使用用户指定的叶节点名称。

    注意：
        该函数与`to_newick`一起使用

    参数:
        node (HashableClusterNode): 从层次聚类连接矩阵输出的根节点
        parentdist (float): `node`的父节点的距离
        newick (list of string): Newick字符串输出累加器列表，需要反转并连接（即`''.join(newick)`）以获得最终输出
        leaf_names (list of string): 叶节点的名称

    返回:
        (list of string): 返回Newick输出字符串的列表
    """
    if node.is_leaf():
        # 如果节点是叶节点，直接返回叶节点名称和距离
        return newick + [f'{str(leaf_names[node.id])}:{parentdist - node.dist}']

    # 如果newick列表不为空，添加右括号和节点距离
    if len(newick) > 0:
        newick.append(f'):{parentdist - node.dist}')
    else:
        newick.append(');')

    # 递归处理左子节点
    newick = _scipy_tree_to_newick_list(node.get_left(), newick, node.dist, leaf_names)
    # 添加逗号分隔符
    newick.append(',')
    # 递归处理右子节点
    newick = _scipy_tree_to_newick_list(node.get_right(), newick, node.dist, leaf_names)
    # 添加左括号
    newick.append('(')
    
    return newick

def to_newick(node, parentdist, leaf_names):
    """将SciPy层次聚类ClusterNode转换为Newick格式字符串

    参数:
        node (scipy.cluster.hierarchy.ClusterNode): 从层次聚类连接矩阵输出的根节点
        parentdist (float): `node`的父节点的距离
        leaf_names (list of string): 叶节点的名称

    返回:
        (string): Newick格式的字符串
    """
    def convert_to_hashable(node):
        """递归转换 ClusterNode 为 HashableClusterNode"""
        if node is None:
            return None
        return HashableClusterNode(
            node.id, 
            node.dist, 
            node.count, 
            convert_to_hashable(node.left), 
            convert_to_hashable(node.right)
        )
    
    # 将输入的ClusterNode转换为可哈希的ClusterNode
    # hash_node = convert_to_hashable(node)
    # 获取Newick字符串列表
    newick_list = _scipy_tree_to_newick_list(node, [], parentdist, leaf_names)
    # 连接并返回Newick字符串
    return ''.join(newick_list)

#  Example usage:
import pandas as pd
from scipy.cluster.hierarchy import linkage

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Normalize the dataframe
# normalized_df = (df - df.mean()) / df.std()
scaler = StandardScaler()
normalized_df = scaler.fit_transform(df)
# Generate the linkage matrix
Z = linkage(normalized_df, method='weighted', metric='euclidean')

# Generate the clustering tree
T = to_tree(Z, rd=False)

# Define the leaf names
leaf_names = df.index.tolist()

# Get the Newick format string
newick_str = to_newick(T, T.dist, leaf_names)
print(newick_str)


def to_newick(node, parentdist, leaf_names):
    """Convert a hierarchical clustering tree to Newick format string.
    
    Args:
        node (scipy.cluster.hierarchy.ClusterNode): Root node is output of scipy.cluster.hierarchy.to_tree from hierarchical clustering linkage matrix
        parentdist (float): Distance of parent node of `node`
        leaf_names (list of string): Leaf node names
    
    Returns:
        str: Newick format string
    """
    return ''.join(_scipy_tree_to_newick_list(node, parentdist, leaf_names)) + ';'

# Example usage:
import pandas as pd
from scipy.cluster.hierarchy import linkage

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Normalize the dataframe
normalized_df = (df - df.mean()) / df.std()

# Generate the linkage matrix
Z = linkage(normalized_df, method='weighted', metric='euclidean')

# Generate the clustering tree
T = to_tree(Z, rd=False)

# Define the leaf names
leaf_names = df.index.tolist()

# Get the Newick format string
newick_str = to_newick(T, T.dist, leaf_names)
print(newick_str)