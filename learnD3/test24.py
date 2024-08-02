import pandas as pd
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import to_tree
from functools import lru_cache
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

# 假设你的数据框 normalized_df 已经存在，并且包含了需要聚类的数据
# 例如：
normalized_df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['Sample1', 'Sample2', 'Sample3'])

# 进行层次聚类
Z = hierarchy.linkage(normalized_df, method='weighted', metric='euclidean')
T = to_tree(Z, rd=False)

# 创建一个全局变量来存储节点
nodes = {}

def cache_node(node):
    """缓存节点对象"""
    if node.id not in nodes:
        nodes[node.id] = node
    if not node.is_leaf():
        cache_node(node.get_left())
        cache_node(node.get_right())

# 缓存所有节点
cache_node(T)

@lru_cache(maxsize=None)
def _scipy_tree_to_newick_list(node_id, parentdist, leaf_names):
    """从SciPy层次聚类ClusterNode构建Newick树（使用缓存优化的递归实现）

    参数:
        node_id (int): 当前节点的唯一标识符
        parentdist (float): `node`的父节点的距离
        leaf_names (list of string): 叶节点的名称

    返回:
        (list of string): 返回Newick输出字符串的列表
    """
    node = nodes[node_id]
    if node.is_leaf():
        # 如果节点是叶节点，直接返回叶节点名称和距离
        return [f'{str(leaf_names[node.id])}:{parentdist - node.dist}']

    # 递归处理左子节点
    left_newick = _scipy_tree_to_newick_list(node.get_left().id, node.dist, leaf_names)
    # 递归处理右子节点
    right_newick = _scipy_tree_to_newick_list(node.get_right().id, node.dist, leaf_names)

    newick = [f'({",".join(left_newick)},{",".join(right_newick)})']

    return newick + [f':{parentdist - node.dist}']

def to_newick(tree, leaf_names):
    """将树结构转换为 Newick 格式"""
    # 获取 Newick 格式的字符串
    newick_list = _scipy_tree_to_newick_list(tree.id, tree.dist, tuple(leaf_names))
    return ''.join(newick_list) + ';'
def to_newick(node, parentdist, leaf_names):
    """将树结构转换为 Newick 格式"""
    if node.is_leaf():
        return f'{leaf_names[node.id]}:{parentdist - node.dist}'

    left_newick = to_newick(node.get_left(), node.dist, leaf_names)
    right_newick = to_newick(node.get_right(), node.dist, leaf_names)

    return f'({left_newick},{right_newick}):{parentdist - node.dist}'
def to_newick(tree, leaf_names):
    """将树结构转换为 Newick 格式"""
    # 获取 Newick 格式的字符串
    newick_list = _scipy_tree_to_newick_list(tree.id, tree.dist, tuple(leaf_names))
    return ''.join(newick_list[::-1]) + ';'

# 获取行名
row_names = list(normalized_df.index)

# 将树结构转换为 Newick 格式
newick_str = to_newick(T, row_names) + ';'
# 获取行名
row_names = list(normalized_df.index)

# 将树结构转换为 Newick 格式
# newick_str = to_newick(T, row_names)

# 将 Newick 格式的字符串写入文件
# with open("output_tree.newick", "w") as f:
#     f.write(newick_str)

print(f"Newick format tree written to output_tree.newick:\n{newick_str}")