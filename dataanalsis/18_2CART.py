# !/usr/bin/python3
# <--encoding=utf-8-->

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# prepare the dataset
boston = load_boston()
# dig the data
print(boston.feature_names)
# get the character set and house prices
features = boston.data
prices = boston.target

# randomly sample 33% dataset as test group, other as train set
train_features, test_features, train_price, test_price = train_test_split(features, prices, test_size=0.33)

# create the CART regression tree
dtr = DecisionTreeRegressor()
# fitting and construct regression tree
dtr.fit(train_features, train_price)

# predict the price of house in test group
predict_price = dtr.predict(test_features) 

# evalute the result of test group
print('回归树二乘偏差均值:',mean_squared_error(test_price, predict_price))
print('回归树绝对偏差均值:', mean_absolute_error(test_price, predict_price))

