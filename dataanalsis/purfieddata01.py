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




