# !/usr/bin/python3
# <!--encoding='utf-8'-->

from sklearn import tree
import sys
import os
import graphviz
import numpy as np

os.environ["PATH"] += os.pathsep + 'D:/Download/Graphviz/bin'
# create the dataset[red,big] ,1==True, 0== False
data = np.array([[1,1],[1,0],[0,1],[0,0]])

# set the sign as, 1==good apple;0==bad apple
target = np.array([1,1,0,0])

# create the model
clf = tree.DecisionTreeClassifier()

# fitting the data
clf = clf.fit(data, target)

# finally use graphviz to print out target tree
dot_data = tree.export_graphviz(clf,out_file=None)
graph = graphviz.Source(dot_data)
graph.view()
print(graph)




