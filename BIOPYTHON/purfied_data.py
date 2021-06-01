# !/usr/python3
# encoding = utf-8
import os 




mode = 'r'
fileinput = open("../data/test.fasta", encoding='utf-8')

# 1.判断正确的fasta文件格式




# 2.去除'-',提取对比的序列
# print(fileinput.readline())
fileinput.readline()
line = fileinput.read()
count = line.replace('\n', '')
count = count.split('-')

count = [i for i in count if i !='']

# print(count[0:10])
print(count)
# 3.输出文件到数据库
# 单独使用试试。。







fileinput.close()





