# !/usr/bin/python3
# -*- coding:utf-8 -*-

# use csv module to handle tsv file to draw images
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from networkx.algorithms.link_analysis.pagerank_alg import pagerank
# from pandas import DataFrame 
# from sklearn.cluster import KMeans

# df = pd.read_csv('../data/result_cluster.tsv', delimiter='\t',names=['1','2'])
# print(df)
# outfile = open("./result.csv",mode="a+")
# outfile = csv.writer(outfile)
# df.to_csv("./result_cluster.csv",sep=',', index=False)
# 1.transform key into set group 
# print(df[1])
# 2. We get the all names, than write it into databse
df = pd.read_csv('./result_cluster.csv', delimiter='\t',names=['1','2'])
x = set([i.split(',')[0] for i in df['1']])
print(len(x))


# 创建有向图
# G = nx.DiGraph()
G = nx.MultiGraph()
# 有向图之间边的关系
# edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
edges = [tuple(i.split(',')) for i in df['1'].head(100)]
for edge in edges:
    G.add_edge(edge[0], edge[1])

# pagerank_list = nx.pagerank(G, alpha=0.7)

# print("pagerank值是: ", pagerank_list)

# nx.draw(G,pos = nx.random_layout(G), node_color = 'w',edge_color = 'r',
#         with_labels = True, font_size =18,node_size =20)

# https://networkx.org/documentation/stable/auto_examples/drawing/plot_four_grids.html#sphx-glr-auto-examples-drawing-plot-four-grids-py
# adjust iterations to make line longer
pos = nx.spring_layout(G,iterations=45) 

nx.draw(G, pos,  node_color = 'r',edge_color = 'r', alpha = 0.7, width = 3,
        with_labels = True, font_size = 4,node_size = 30,cmap=plt.cm.Dark2, # matplotlib的调色板，可以搜搜，很多颜色呢
        edge_cmap=plt.cm.Blues)
# for p in pos:  # raise text positions
#     pos[p][1] += 0.07
# nx.draw_networkx_labels(G, pos)

plt.show()
# print(x)
# print(len(x))
# 3.draw a matirx to show its correlationship






# y = np.random.randint(1,100,40)
# y = y.reshape((5,8))
# df = pd.DataFrame(y,columns=[x for x in 'abcdefgh'])
# sns.heatmap(df,annot=True)
# sns.heatmap(df)
# plt.show()

# print(pd.read_csv('file.tsv', delimiter='\t'))

# with open('../data/result_cluster.tsv') as f:
#     tsvreader = csv.reader(f, delimiter='\t')
#     for line in tsvreader:
#         print(line)



