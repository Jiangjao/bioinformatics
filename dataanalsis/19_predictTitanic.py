# !/usr/bin/python3
# <!--encoding='utf-8'-->

from sklearn import tree
import sys
import os
import graphviz
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
# prepare the dataset
iris=load_iris()

# get the feature set and classified sign
features = iris.data
labels = iris.target

# randomly handle 33% of data as test group, other as training group
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
# create the CART tree
clf = DecisionTreeClassifier(criterion="gini")
# print(clf.__dict__)

# fitting and construct tree
clf = clf.fit(train_features, train_labels)

# load the data
train_data = pd.read_csv('../data/train.csv')
test_data = pd.read_csv('../data/test.csv')

# data seek 
print(train_data.info())
print('-'*30)
print(train_data.describe())
print('-'*30)
print(train_data.describe(include=['O']))
print('-'*30)
print(train_data.head())
print('-'*30)
print(train_data.tail())

# use the average age to fill in the non-value
train_data["Age"].fillna(train_data["Age"].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)

# use the fare tickets mean to fill in the fare non-value
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

# look around the value of Embarked
print(train_data["Embarked"].value_counts())

# use the most embark to fill out the nan value of the embark port
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)


# select characters
features = ["Pclass", "Sex", "Age", "Sibsp", "Parch", "Fare", "Embarked"]
train_features = train_data[features]
train_labels = train_data["Survived"]
test_features = test_data[features]

