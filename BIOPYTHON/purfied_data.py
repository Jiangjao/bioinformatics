# !/usr/python3
# encoding = utf-8
import os
import sys
from time import sleep 
from insert_mysql import innerSql

def openfilelist(path):
    files = []
    if os.path.exists(path):
        files = [filenames for filepath,dirnames,filenames in os.walk(path,topdown=True) if filenames]
        if len(files): files=os.listdir(path)
        print(files)         
    else:
        print('this path not exist')
    
    # print(os.walk(path))
    
    # if len(files) < 1:

    return files

def handlefile(fileinput):
    """
    separate '-' in file and transform it into segement.

    :param fileinput: file stream
    :return :filename:str; count: nest list
    """
    # 1.判断正确的fasta文件格式
    fileline = fileinput.readline()
    firstline = fileline
    if fileline.startswith(">"):
        temp = fileinput.readline()
        secondline = temp
        while not temp.startswith(">"):
            temp = fileinput.readline()
            # arrive the end of file, then break down
            if not temp:
                print("we arrive the EOF")
                break
        print("the real fasta we want to get")

    # 2.去除'-',提取对比的序列
    # print(temp,firstline)
    line = fileinput.read()
    count = line.replace('\n', '')
    count = count.split('-')
    count = [i for i in count if i !='']

    print(count)
    # Rice_virus_segment_alignment =  os.path.basename(filename)

    # get the alignment segement name of virus and rice
    Rice_virus_segment_alignment =  str(firstline + temp).replace("\n","")
    clearFile(Rice_virus_segment_alignment, count)
    # print(Rice_virus_segment_alignment)
    return Rice_virus_segment_alignment, count

def clearFile(Rice_virus_segment_alignment,count):
    """
    drop the null file and write down just handle.

    :param :filename:str; count:list
    :stdout: local files
    """
    if len(count[0]) < 5:
        print(Rice_virus_segment_alignment, file="unhandlefiles.txt")
    
if __name__ == '__main__':
    mode = 'r'
    # filename = "../notes/virus_segement1_NC_02925613.1.fa"
    # 从命令行获取参数，filename 实际上可以获取为
    # fullpath = sys.argv[1]
    # prefullpath
    fullpath = '‪C:/Users/Cherry/Desktop/result/'
    groupfiles = openfilelist(fullpath)
    # os.path.abspath()
    print(groupfiles)
    for filename in groupfiles:
        fileinput = open(fullpath + filename , mode=mode, encoding='utf-8')
        bracket = handlefile(fileinput)
        key = bracket[0]
        values = bracket[1]
        print(key,values)
        for element in values:  
            # 3.输出文件到数据库
            innerSql(key,  element)
        sleep(1)
        # print(bracket)
        fileinput.close()













