# -!--coding='utf-8'--
from efficient_apriori import apriori
import csv

# 设置数据集
# data = [('牛奶','面包','尿布'),  
#     ('可乐','面包', '尿布', '啤酒'),           
#     ('牛奶','尿布', '啤酒', '鸡蛋'),
#     ('面包', '牛奶', '尿布', '啤酒'),           
#     ('面包', '牛奶', '尿布', '可乐')]

# 挖掘频繁项集和频繁规则
# itemset, rules = apriori(data, min_support=0.5, min_confidence=1)
# print(itemset)
# print(rules)

lists = csv.reader(open("../data/nihaodirector.csv", encoding='utf-8'))
# 数据加载
data = []
for names in lists:
    name_new = []
    for name in names:
        # 去掉演员数据中的空格
        name_new.append(name.strip())
    data.append(name_new[1:])
# 挖掘频繁项集和关联规则
itemsets, rules = apriori(data, min_support=0.5, min_confidence=1) 
print(itemsets)
print(rules)








