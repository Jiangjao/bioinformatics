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
