# !/usr/python3
# <-- encoding=utf-8 -->

# 在sklearn中使用SVM算法
# SVM做回归的时候，就可以使用SVR和LinearSVR
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

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

# 特征选择

# 特征选择
features_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean'] 
# 抽取30%的数据作为测试集，其余作为训练集
# in this our main data is splitted into train and test
train, test = train_test_split(data, test_size=0.3)
# 抽取特征选择的数值作为训练和测试数据
train_X = train[features_remain]
train_y = train['diagnosis']
test_X = test[features_remain]
test_y = test['diagnosis']

# 规范化数据到同一量级上
# 采用Z-Score规范化数据，保证每个特征维度的数据均值为0，方差为1
ss = StandardScaler()
train_X = ss.fit_transform(train_X)
test_X = ss.transform(test_X)
# 创建SVM分类器
model = svm.SVC()
# 用训练集做训练
model.fit(train_X, train_y)
# 用测试集做预测
prediction = model.predict(test_X)
print("准确率:",metrics.accuracy_score(test_y,prediction))


