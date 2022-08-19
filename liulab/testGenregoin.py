'''
Author: jayjiao 918718278@qq.com
Date: 2022-08-18 17:24:01
LastEditors: jayjiao 918718278@qq.com
LastEditTime: 2022-08-19 14:29:09
FilePath: \geekbang\bioinformatics\liulab\testGenregoin.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# !/usr/bin/python3
# author:xiaojiao 2022/08/18
# split chrome length into range between region(500000)

chromeinfo = [ ("Chr1 ",   222834174), ("Chr2 ",   213184539), \
("Chr11",   123678568), ("Chr12",   162709580), \
("Chr13",   136142203), ("Chr14",   133855197), \
("Chr15",   119080728), ("Chr3 ",   187390788), \
("Chr4 ",   196298966), ("Chr5 ",   194877589), \
("Chr6 ",   181129525), ("Chr7 ",   187104375), \
("Chr8 ",   163071019), ("Chr9 ",   165547432), \
("Chr10",   167113155)]



def genregion(chromeinfo:list):
    for chromes in chromeinfo:
        chrome, length   = chromes
        step = 500000
        flag = 0
        if chrome.strip() == "Chr1":
            # yield (0, chrome)
            for regoin in range(step, length, step):
                # print(regoin, chrome)
                # yield (flag, regoin, chrome)
                yield "SELECT * from testGWAS WHERE " + " regoin >= " + str(flag) \
                    + " AND regoin <= " + str(regoin) + " AND chrome=" + chrome
                if (regoin + step) >= length:
                    flag = 0
                else:
                    flag += step

ss = genregion(chromeinfo)

print(next(ss))
print(next(ss))