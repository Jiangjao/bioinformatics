# !/usr/python3
# <-- encoding=utf-8 -->

from operator import concat
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np 

# 输入数据
data = pd.read_csv('../data/data.csv', encoding='utf-8')
train_x = data[[u"2019年国际排名",u"2018世界杯",u"2015亚洲杯"]]
df = pd.DataFrame(train_x)

# 每次输出的结果不尽相同..
kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=300, 
    tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, 
    copy_x=True, n_jobs=1, algorithm='auto')
# kmeans = KMeans(n_clusters=5)
# 规范到[0, 1]空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# kmeans算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)



