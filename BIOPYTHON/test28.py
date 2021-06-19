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

df = pd.read_csv('../data/Rice_chrome_viruspart01.csv',names=['1','2','3'])
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
pre_x = [ i[:13]  for i in df['3']]
# print(pre_y)
x = np.array(pre_x) 
y = np.array(df['2'])
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
s = np.random.rand(*x.shape) * 10 + 50

# volin plot is also ready.....
print(df['2'].quantile(0.75))
z = np.array(df['2'].mean())
# plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")

# plt.violinplot(x, y)
# fig,axes = plt.subplots(nrows=1,ncols=1,figsize=(12,5))
# tang_data = [np.random.normal(0,std,100) for std in range(6,10)]
ax = sns.violinplot(x=x,y=y,showmeans=False,showmedians=True,palette="Pastel1",
		scale='count',inner='box',color='green')

# ax.show()
# fig, axes = plt.subplots(nrows=1,ncols=2, figsize=(12,5))
 
# # all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
# all_data = y 
# #fig = plt.figure(figsize=(8,6))
 
# axes[0].violinplot(all_data,
#                showmeans=False,
#                showmedians=True
#                )
# axes[0].set_title('violin plot')
 
# axes[1].boxplot(all_data,)
# axes[1].set_title('box plot')
 
# # adding horizontal grid lines
# for ax in axes:
#     ax.yaxis.grid(True)
#     ax.set_xticks([y+1 for y in range(len(all_data))], )
#     ax.set_xlabel('xlabel')
#     ax.set_ylabel('ylabel')
 
# plt.setp(axes, xticks=[y+1 for y in range(len(all_data))],
#         xticklabels=x,
#         )

# 平均值是多少来着？
# print(df['2'].mean())
# 画出 y=1 这条水平线
# plt.axhline(z,color='red',linewidth=1,linestyle='--')
# plt.plot(x,z,color='red',linewidth=1,linestyle='--')

# plt.xlabel("chromesomes")
# plt.ylabel("length of segements")
# plt.legend(loc='upper left')
plt.xticks(rotation=30) # 倾斜70度
plt.grid(axis="y")
plt.show()


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
# print(df.index)
# print(df.head())
# print(df.index[:5])
# plt.figure(figsize=(100, 100), dpi=100)
# plt.scatter(x, y)
# plt.savefig('test01.svg')
# plt.show()

# if we use seaborn to draw the violin image of dataset
# it wil be easier to look at 
# but we cannot kook up globally
