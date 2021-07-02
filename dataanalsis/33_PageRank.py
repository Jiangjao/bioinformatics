# !/usr/bin/python3
# -*- coding:utf-8 -*-

# import networkx as nx
# from networkx.algorithms.link_analysis.pagerank_alg import pagerank
# # 创建有向图
# G = nx.DiGraph()
# # 有向图之间边的关系
# edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
# for edge in edges:
#     G.add_edge(edge[0], edge[1])
# pagerank_list = nx.pagerank(G, alpha=1)
# print("pagerank值是: ", pagerank_list)

# 用PageRank 挖掘希拉里邮件中的重要任务关系
import pandas as pd
import networkx as nx
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
# 数据加载
emails = pd.read_csv("../data/input/Emails.csv")
# 读取别名文件
file = pd.read_csv("../data/input/Aliases.csv")
aliases = {}
for index, row in file.iterrows():
    aliases[row["Alias"]] = row['PersonId']    # 
# 读取人名文件
file = pd.read_csv("../data/input/Persons.csv")
persons = {}
for index, row in file.iterrows():
    persons[row['Id']] = row['Name']
# 针对别名进行转换
def unify_name(name):
    # 姓名统一小写
    name = str(name).lower()
    # 去掉，和@后面的内容
    name = name.replace(",","").split("@")[0]
    # 别名转换
    if name in aliases.keys():
        return persons[aliases[name]]
    return name
# 画网络图
def show_graph(graph, layout='spring_layout'):
    # 使用Spring Layout布局，类似中心放射状
    if layout == 'circular_layout':
        positions=nx.circular_layout(graph)
    else:
        positions=nx.spring_layout(graph)
    # 设置网络图中的节点大小，大小与 pagerank 值相关，因为 pagerank 值很小所以需要 *20000







