# !/usr/bin/python3
# <--encoding=utf-8-->
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# prepare the dataset
iris=load_iris()

# get the feature set and classified sign
features = iris.data
labels = iris.target

# randomly handle 33% of data as test group, other as training group
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
# create the CART tree
clf = DecisionTreeClassifier(criterion="gini")
# fitting and construct tree
clf = clf.fit(train_features, train_labels)
# use CART tree to predict
test_predict = clf.predict(test_features)
# compare the predict result with test result
score = accuracy_score(test_labels, test_predict)
print("CART分类树准确率 %.4lf" % score)















