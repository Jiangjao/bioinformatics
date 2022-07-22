from __future__ import print_function, division
from pickletools import uint1
# from re import ASCII
import numpy as np
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import cchardet as chardet
import base64
# import bytearray
# import vcfnp
filename = './data/ss.vcf.gz'
# from collections import ChainMap 
# baseline = {'music': 'bach', 'art': 'rembrandt'}
# adjustments = {'art': 'van gogh', 'opera': 'carmen'}
# test = ChainMap(adjustments, baseline)
# ChainMap({'art': 'van gogh', 'opera': 'carmen'}, {'music': 'bach', 'art': 'rembrandt'})
# list(ChainMap(adjustments, baseline))
# ['music', 'art', 'opera']

# dcic1 = {'label1': '11', 'label2': '22'}
# dcic2 = {'label2': '22', 'label3': '33'}
# dcic3 = {'label4': '44', 'label5': '55'}
# last  = ChainMap(dcic1, dcic2,dcic3)
# last  
# ChainMap({'label1': '11', 'label2': '22'}, {'label2': '22', 'label3': '33'}, {'label4': '44', 'label5': '55'})
# print(test)
# ss = test.get("art")
# print(ss)
# test.get("")


# print(vcfnp.__version__)
print(filename)
# load vcf file..
# v = vcfnp.variants(filename, cache=False).view(np.recarray)
# fig = plt.figure(1)
# ax = fig.add_subplot(111)
# ax.hist(v.DP)
# plt.show()
# so need to drop INFO	FORMAT	NORMAL	tumor.chr20
import allel
# allel.vcf_to_hdf5(filename, "./data/ss8.h5", fields='*', exclude_fields=["tumor.chr20", "info"], \
#                     vlen=False, compression="gzip",shuffle=True,compression_opts=9)

import h5py
import collections
# so need to read as a dataframe?
# use pytable?
totalPos = [129805, 129815, 193314, 272757, 331922, 341922]
callset = h5py.File("./data/ss5.h5", mode="r")
print(callset.keys())
chrom = callset["variants/CHROM"]
ref = callset["variants/REF"]
pos = callset["variants/POS"]
alt = callset["variants/ALT"]
start = 1
end = 5
# print(chrom[start:end], sep=",")
chrom2 = chrom[start:end]
ref2 = ref[start:end]
pos2 = list(pos[start:end])
alt2 = alt[start:end]

print("alt")
print(alt2.tostring())

encode_type = chardet.detect(alt2.tostring())
print(encode_type)
alt2CleanPre = alt2.tostring().decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）

temp = str(alt2CleanPre).strip().strip('\x00')
# print(str(alt2CleanPre).strip().strip('\x00'))
print(temp)
print("2233")
# so how to remove \x00
# https://stackoverflow.com/questions/38883476/how-to-remove-those-x00-x00
alt2Clean = [i for i in temp if i != "\x00"]
print(alt2Clean)

# chromArray = np.fromstring(chrom2)
# print(chromArray)


# print(refArray)
# chromArray = np.fromstring(chrom2, sep=",", dtype=int)
# refArray = np.fromstring(ref2, sep=",", dtype=str)
# print(list(ref2))

# temp = bytearray(ref2)
# print(ref2.tostring())
# print(list(pos2))
# nn = base64.b64decode(chromArray).decode("ascii")
# print(nn,'22')
# a = np.array(np.frombuffer(ref2, dtype=str));
# print(list(a))

# how to convert byte-array into list
# print(list(chrom[start:end])[0])
# element = list(chrom[start:end])[0]
# print(element)
# print(type(element))
# chrom[:].asstr
# print(chrom[:].dtype)
# print(ref[:].tostring())

print(ref2.tostring())
encode_type = chardet.detect(ref2.tostring())

m = ref2.tostring().decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）

# encode_typeposSample01 = chardet.detect(pos2.tostring())
# print(encode_typeposSample01)
# posSample01 = pos2.tostring().decode(encode_typeposSample01['encoding'])
# how to zip ref / alt in collections vs. total ref
# zip(m, chrom.tostring())
print(len(m))
# print(posSample01)
print(len(list(pos2)))

# totalPos difference bwtween pos
# how faster if use dataframe?
differencea = set(totalPos).difference(set(list(pos2)))
cc = [list(totalPos).index(i) for i in differencea]
print(differencea)
print(cc)

for index in cc:
    posFinal = pos2.insert(index, "")
    alt2Clean.insert(index, "")

print(list(pos2))
print(alt2Clean)
# calldata = callset["calldata"]
# samples = callset["samples"]
# print(calldata)
# print(samples)