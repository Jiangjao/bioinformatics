# !/usr/python3
# encoding = utf-8
import os
import sys
from time import sleep 

filename = "../data/test.fasta"
fileinput = open("../data/test.fasta", "r")
fileline = fileinput.readline()
firstline = fileline
if fileline.startswith(">"):
    temp = fileinput.readline()
    secondline = temp
    while not temp.startswith(">"):
        temp = fileinput.readline()
        if not temp:
            print("we arrive the end")
            break
    print("the real fasta we want to get")

    Rice_virus_segment_alignment =  str(firstline + temp).replace("\n","").replace('>', ">")
    # print(Rice_virus_segment_alignment)

    line = fileinput.read()
    count = line.replace('\n', '')
    count = count.split('-')
    count = [i for i in count if i !='']
# print(count,firstline,temp)
print(Rice_virus_segment_alignment)
# filename, count = puredata.handlefile(fileinput)
# print(count)