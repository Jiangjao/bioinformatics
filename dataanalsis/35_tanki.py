# !/usr/bin/python3
# -- coding: utf-8 --

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.feature_extraction import DictVectorizer

# load data
train_data = pd.read_csv("../data/train.csv")
test_data = pd.read_csv("../data/test.csv")

# 2.clean data
# use average age to fill in the NAN value
train_data["Age"].fillna(train_data["Age"].mean(), inplace=True)
test_data["Age"].fillna(test_data["Age"].mean(), inplace=True)
# average fare to fill in
train_data["Fare"].fillna(train_data["Age"].mean(),inplace=True)
test_data["Fare"].fillna(test_data["Fare"].mean(), inplace=True)
# use the most landing port to fill in
train_data["Embarked"].fillna('S',inplace=True)
test_data["Embarked"].fillna('S',inplace=True)

# choose the features
features = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
train_features=train_data[features]
train_labels=train_data["Survived"]
test_features=test_data[features]

# normalize the object of Embarked to 0/1
dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
test_features=dvec.transform(test_features.to_dict(orient='record'))

# decisiontree classifier
dt_stump = DecisionTreeClassifier(max_depth=1,min_samples_leaf=1)
dt_stump.fit(train_features, train_labels)

print(u'决策树分类器准确率%.4lf' % np.mean(cross_val_score(dt_stump,train_features, 
        train_labels,cv=10)))

dt = DecisionTreeClassifier()
dt.fit(train_features, train_labels)

print(u'决策树分类器准确率为%.4lf' % np.mean(cross_val_score(dt, 
        train_features, train_labels,cv=10)))

#  AdaBoost classfied
ada = AdaBoostClassifier(base_estimator=dt_stump, n_estimators=200)
ada.fit(train_features,train_labels)

print('AdaBoost分类器准确率为%.4lf'%np.mean(cross_val_score(ada,
            train_features,train_labels,cv=10)))







