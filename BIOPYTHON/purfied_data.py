# !/usr/python3
# encoding = utf-8
import os
import sys
from time import sleep 
from insert_mysql import innerSql

def openfilelist(path):
    files = []
    print(os.path.abspath(path))
    if os.path.exists(path):
        files = [filenames for filepath,dirnames,filenames in os.walk(path,topdown=True) if filenames]
        # if len(files): files=os.listdir(path)
        print(files)         
    else:
        print('this path not exist')
    
    # print(os.walk(path))
    
    # if len(files) < 1:

    return files, os.path.abspath(path)

def handlefile(fileinput):
    """
    separate '-' in file and transform it into segement.

    :param fileinput: file stream
    :return :filename:str; count: nest(segement) list;firstline, temp：random (rice , virus)
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
    return Rice_virus_segment_alignment, count,firstline, temp

def clearFile(Rice_virus_segment_alignment,count):
    """
    drop the null file and write down just handle.

    :param :filename:str; count:list
    :stdout: local files
    """
    # print(count)
    try:
        if len(count[0]) < 2:
            print(Rice_virus_segment_alignment, open("unhandlefiles.txt","a+"))
    except IndexError:
        print(Rice_virus_segment_alignment, file=open("unhandlefiles.txt",'a+'))
    
if __name__ == '__main__':
    mode = 'r'
    # filename = "../notes/virus_segement1_NC_02925613.1.fa"
    # 从命令行获取参数，filename 实际上可以获取为
    # fullpath = sys.argv[1]
    # prefullpath

    # I don't understand why we can't use absolute path here.
    fullpath = r'‪../../../../result'
    groupfiles, fullpath = openfilelist(fullpath)
    fullpath = 'C:/Users/Cherry/Desktop/geekbang/result/'
    # os.path.abspath()
    print(groupfiles)
    for filename in groupfiles[0]:
        fileinput = open(fullpath + filename , mode=mode, encoding='utf-8')
        bracket = handlefile(fileinput)
        key = bracket[0]
        count = bracket[1]
        firstline = bracket[2]
        temp = bracket[3]
        print(key,count)
        for element in count:  
            # 3.输出文件到数据库
            innerSql(key,  element, firstline, len(element), temp)
        sleep(1)
        # print(bracket)
        fileinput.close()













