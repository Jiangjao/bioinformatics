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

data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['Sample1', 'Sample2', 'Sample3'])
# Normalize the dataframe
# heatmap_file = "C:/Users/Cherry/Downloads/circle_heatmap_chart_heatmap_file.txt"
heatmap_file = "C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/heatmap2.txt"
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

@lru_cache(maxsize=128)
def _scipy_tree_to_newick_list(node_id, parentdist, leaf_names):
    """从SciPy层次聚类ClusterNode构建Newick树（缓存版本）

    参数:
        node_id (int): 当前节点的唯一标识符
        parentdist (float): `node`的父节点的距离
        leaf_names (list of string): 叶节点的名称

    返回:
        (list of string): 返回Newick输出字符串的列表
    """
    node = nodes[node_id]
    if node.is_leaf():
        return [f'{str(leaf_names[node.id])}:{parentdist - node.dist}']

    left_newick = _scipy_tree_to_newick_list(node.get_left().id, node.dist, leaf_names)
    right_newick = _scipy_tree_to_newick_list(node.get_right().id, node.dist, leaf_names)

    return [f'({",".join(left_newick)},{",".join(right_newick)})'] + [f':{parentdist - node.dist}']

def to_newick(node, parentdist, leaf_names):
    """将树结构转换为 Newick 格式"""
    # parentdist = node.dist
    if node.is_leaf():
        return f'{leaf_names[node.id]}:{parentdist - node.dist}'

    left_newick = to_newick(node.get_left(), node.dist, leaf_names)
    right_newick = to_newick(node.get_right(), node.dist, leaf_names)

    return f'({left_newick},{right_newick}):{parentdist - node.dist}'

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



# 将树结构转换为 Newick 格式
newick_str = to_newick(T, T.dist, row_names)

# 将 Newick 格式的字符串写入文件
# with open("output_tree.newick", "w") as f:
#     f.write(newick_str)
# 去除根节点的距离信息
newick_str = newick_str.rstrip('):0.0') + ';'
print(f"Newick format tree written to output_tree.newick:\n{newick_str}")


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
# ((1:2.1213203435596424,0:2.1213203435596424):1.0606601717798214,2:3.181980515339464);
# ((1:2.1213203435596424,0:2.1213203435596424):1.0606601717798214,2:3.181980515339464);
# (2:3.181980515339464,(0:2.1213203435596424,1:2.1213203435596424),:1.0606601717798214):0.0;
# :0.0(Sample3:2.598076211353316,(Sample1:1.7320508075688772,Sample2:1.7320508075688772),:0.8660254037844388);
