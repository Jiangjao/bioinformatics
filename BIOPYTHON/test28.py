# -!--coding='utf-8'--
# use squences to draw image on each chromesome
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# "数据对齐是内在的"
# Series是带标签的一维数组
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series(np.random.random(5), index=['a','b','c','d','e'])
print(s)
print(s.index)
print(s['a'])

sites = {1:"Google", 2:"Runoob", 3:"Wiki"}
myvar = pd.Series(sites, index=[1,2,3])


myvar2 = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST")



print(myvar[3])
print(myvar2)

data = [['Google', 10],['Runoob', 12],['Wiki', 13]]
df = pd.DataFrame(data,columns=['Site','Age'], dtype=float)


print(df)

data = {'Site':['Google', 'Runoob','Wiki'],'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print(data)

data = [{'a':1, 'b':2},{'a':5,'b':10,'c':20}]
df = pd.DataFrame(data)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

print(data)
print(df.loc[0])
print(df.loc[1])
print(df.loc[[0, 1]])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ['day1','day2','day3'])
print(df)

# 指定索引
print(df.loc["day2"])

df = pd.read_csv('../data/testRice01.csv',names=['1','2','3'])
# df = pd.DataFrame(df,index=['1','2','3'])
# print(df.to_string())
# print(df)
# print(df.head(10))
# print(df.tail(10))
print(df.info())

# print(df['3'].index[12239])

# 打印最长的几行
print(df['3'].sort_values(key=lambda x: x.str.len()).tail(20))
print(df['3'].tail().values)

# 打印行
print(df['1'].iloc[:10])
# 依据序列的长度，进行排序
pre_y = [ i  for i in df['3'].iloc[:10]]
# print(pre_y)
x = np.array(df['1']) 
y = np.array(df['3'])
# print(df.index[12239])
# print(df.describe())
# print(df.index[12239])


# 打印到最长的几行，并写入文件
# print(df.loc[12239].values,file=open("transforfile.txt", "a+"))

# for i in df.loc[12239].values[2]:
# bracket = [i for i in df.loc[12239].values]
# print(bracket)
# print(len((bracket)[2]))



# draw image

# Fixing random state for reproducibility
# np.random.seed(19680801)


# x = np.arange(0.0, 50.0, 2.0)
# y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
# s = np.random.rand(*x.shape) * 800 + 500

# plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc='upper left')
# plt.show()

# sns.load()
# Load Dataset
# rice = sns.load_dataset('testRice01',data_home='../data',cache=True)
# # rice = sns.load('../data/iris')
# # 用Seaborn画成对关系
# sns.pairplot(rice)
# plt.show()


# print(df['1'])
# print(df['2'])
# print(df['3'])
print(df.head())
plt.figure(figsize=(100, 100), dpi=100)
plt.scatter(x, y)
plt.savefig('test01.svg')
# plt.show()


