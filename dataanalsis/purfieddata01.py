# !/usr/bin/python3
# <!--encoding='utf-8'-->
import pandas as pd
import numpy as np

# read the csv and  load data into dataframe or textparse
dataCount = pd.read_csv("../data/accountMessage.csv",names=['Index','Name','Age','Weight',
                'Male3D01','Male3D02','Male3D03',
                'Female3D01','Female3D02','Female3D03'])

# read th head , tail of data
# print(dataCount.head())
print(dataCount.tail())



# replace the lost age with mean age
dataCount['Age'].fillna(dataCount['Age'].mean(), inplace=True)
print(dataCount)

# if we use the most frequency data to replace the lost Age
# age_maxf = dataCount["Age"].value_counts().index[0]
# dataCount["Age"].fillna(age_maxf, inplace=True)

# ignore the blank line
dataCount.dropna(how="all",inplace=True)
print(dataCount)

# unified the unit of data
# get the column of weight whose unit is lbs
rows_with_lbs = dataCount['Weight'].str.contains('lbs').fillna(False)
print(dataCount[rows_with_lbs])

# transform lbs into kgs, 2.2lbs=1kgs
for i,lbs_row in dataCount[rows_with_lbs].iterrows():
    # cut of the last three characters,i..e cut off lbs
    weight = int(float(lbs_row['Weight'][:-3])/2.2)
    dataCount.at[i, 'Weight'] = '{}kgs'.format(weight)


# cut name into firstname and lastname
dataCount[['first_name','last_name']] = dataCount['Name'].str.split(expand=True)
dataCount.drop('Name', axis=1, inplace=True)


# delete the non-ASCII character
dataCount['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
dataCount['last_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)

# drop out the duplicate data
dataCount.drop_duplicates(['first_name','last_name'],inplace=True)

print(dataCount)

# 学习潘大师如何？？

# 思考题1:对车祸数据成对关系的探索，程序代码如下.
# import matplotlib.pyplot as plt
# import seaborn as sns

# 数据准备
# Loading Pandas DataFrame:
# iris = pd.read_csv('./iris.csv', encoding='windows-1252')
# # iris = sns.load_dataset('iris')  在外网所以不好连接上去
# # 用Seaborn画成对关系
# sns.pairplot(iris)
# plt.show()

# 解决seaborn数据集导入报错的问题
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# # 数据准备
# crashes = sns.load_dataset('car_crashes')
# # crashes_data = pd.DataFrame(crashes)
# print(crashes.head(10))

# # 用Seaborn画成对关系
# sns.pairplot(crashes)
# plt.show()
