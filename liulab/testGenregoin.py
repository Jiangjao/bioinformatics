# !/usr/bin/python3
# author:xiaojiao 2022/08/18
# split chrome length into range between region(500000)

from xml.etree.ElementPath import prepare_self


chromeinfo = [ ("Chr1 ",   222834174), ("Chr2 ",   213184539), \
("Chr11",   123678568), ("Chr12",   162709580), \
("Chr13",   136142203), ("Chr14",   133855197), \
("Chr15",   119080728), ("Chr3 ",   187390788), \
("Chr4 ",   196298966), ("Chr5 ",   194877589), \
("Chr6 ",   181129525), ("Chr7 ",   187104375), \
("Chr8 ",   163071019), ("Chr9 ",   165547432), \
("Chr10",   167113155)]



def genregion(chromeinfo:list):
    # sort chromes in order
    chromeinfo = sorted(chromeinfo, key = lambda x: int(x[0][3:]))
    detailLength = 0
    preLength = 0
    for chromes in chromeinfo:
        chrome, length = chromes
        step = 500000
        flag = 0
        # chrome = chrome.replace("Chr","")

        # get detail length which mapped to x axis
        if length == 222834174 and chrome.strip() == "Chr1":
            # print("emmmmmm")
            preLength = length
        else:
            detailLength = preLength
            preLength += length

        # detailLength += length
        if chrome.strip() != None:
            chrome = chrome.replace("Chr","")
            # yield (0, chrome)
            for regoin in range(step, length, step):
                # print(regoin, chrome)
                # yield (flag, regoin, chrome)

                yield   f'SELECT  `index`, chr,ps, min(p_wald), \' {flag} - {regoin} \' as \'location\' ' \
                        + f', {detailLength} as \'detailX\' ' \
                        + f'from testmgwas WHERE  ps >=  {flag} ' \
                        + f'AND ps <=  {regoin} AND chr={chrome};'
                if (regoin + step) >= length:
                    flag = 0
                else:
                    flag += step
        # SELECT `index`, chr,ps, min(p_wald) from testmgwas WHERE  ps >= 220000000 AND ps <= 220500000 AND chr="Chr"
        # SELECT `index`, chr,ps, min(p_wald),  '148500000-149000000' as "location" \
        #       from testmgwas WHERE  ps >= 148500000 AND ps <= 149000000 AND chr=2;
        yield   f'SELECT  `index`, chr,ps, min(p_wald), \' {regoin} - {length} \' as \'location\' ' \
                    + f', {detailLength} as \'detailX\' ' \
                    + f'from testmgwas WHERE  ps >=  {regoin} ' \
                    + f'AND ps <=  {length} AND chr={chrome};'
        # break

ss = genregion(chromeinfo)
if __name__ =="__main__":
    ss = genregion(chromeinfo)
    for i in ss:
        print(i)
# print(next(ss))
# print(next(ss))