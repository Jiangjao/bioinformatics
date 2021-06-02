# !/usr/python3
# encoding = utf-8
import os
from time import sleep 
from insert_mysql import innerSql

def openfilelist(path):
    files = [filenames for filepath,dirnames,filenames in os.walk(path) if filenames]
       
    return files

def handlefile(fileinput):
    # 1.判断正确的fasta文件格式
    fileline = fileinput.readline()
    firstline = fileline
    if fileline.startswith(">"):
        temp = fileinput.readline()
        while not temp.startswith(">"):
            temp = fileinput.readline()
        print("the real fasta we want to get")

    # 2.去除'-',提取对比的序列
    # print(temp,firstline)
    line = fileinput.read()
    count = line.replace('\n', '')
    count = count.split('-')
    count = [i for i in count if i !='']

    # print(count[0:10])
    # print(count)
    # 3.输出文件到数据库
    # 单独使用试试。。
    Rice_virus_segment_alignment =  os.path.basename(filename)
    # print(Rice_virus_segment_alignment)
    return Rice_virus_segment_alignment, count

if __name__ == '__main__':
    mode = 'r'
    filename = "../notes/virus_segement1_NC_02925613.1.fa"
    fullpath = 'C:/Users/Cherry/Desktop/virus_segement/virus_segement_1/'
    groupfiles = openfilelist(fullpath)[0]
    # os.path.abspath()
    print(groupfiles)
    for filename in groupfiles:
        fileinput = open(fullpath + filename, mode=mode, encoding='utf-8')
        bracket = handlefile(fileinput)
        key = bracket[0]
        values = bracket[1]
        print(key,values)
        for element in values:
            innerSql(key,  element)
        sleep(1)
        # print(bracket)
        fileinput.close()













