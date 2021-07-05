# !/usr/bin/python3
# -*- coding:utf-8 -*-

# 39_40数据挖掘实战（1)：信用卡违约率分析
# 使用 GridSearchCV工具对模型参数进行调优
from sklearn.model_selection import GridSearchCV
# 使用RandomForest对IRIS数据集进行分类
# 利用GridSearchCV寻找最优参数
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
rf = RandomForestClassifier()
parameters = {"n_estimators":range(1,11)}
iris = load_iris()
# 使用GridSearchCV进行参数调优
clf = GridSearchCV(estimator=rf, param_grid=parameters)
# 对iris数据集进行分类
clf.fit(iris.data, iris.target)
print("最优分数： %.4lf" % clf.best_score_)
print("最优参数: ", clf.best_params_)

# pipelines = Pipeline([
#     ('scaler', StandardScaler()),
#     ('pca', PCA()),
#     ('randomforestclassifier', RandomForestClassifier())
# ])
rf = RandomForestClassifier()
parameters = {"randomforestclassifier__n_estimators": range(1,11)}
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('randomforestclassifier', rf )
])
# 使用GridSearchCV进行参数调优
clf = GridSearchCV(estimator=pipeline, param_grid=parameters)
# 对iris数据集进行分类
clf.fit(iris.data, iris.target)
print("最优分数: %.4lf " %clf.best_score_)
print("最优参数: ", clf.best_params_)







