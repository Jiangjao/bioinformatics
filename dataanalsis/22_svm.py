# !/usr/python3
# <-- encoding=utf-8 -->

# 在sklearn中使用SVM算法
# SVM做回归的时候，就可以使用SVR和LinearSVR
from sklearn import svm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../data/cancerdata.csv")
# 数据探索
# 数据集中的列比较多，需要把dataframe中的列全部显示出来
pd.set_option('display.max_columns',None)
print(data.columns)
print(data.head(5))
print(data.describe())

# 将特征字段分成3组
features_mean = list(data.columns[2:12])
features_se = list(data.columns[12:22])
features_worst = list(data.columns[22:32])
# 数据清洗
# id列没有用，删除该列
data.drop("id",axis=1,inplace=True)
# 将B良性的替换为0，M恶性的替换成1
data['diagnosis'] = data['diagnosis'].map({'M':1,'B':0})

# 将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'],label="Count")
plt.show()
# 用热力图呈现features_mean字段之间的相关性
corr = data[features_mean].corr()
plt.figure(figsize=(14,14))
# annot=True显示方格数据
sns.heatmap(corr,annot=True)
plt.show()