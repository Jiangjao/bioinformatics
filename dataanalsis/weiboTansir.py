# -*- coding: utf-8 -*-  
import pandas as pd
import os
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#导入图像处理库
import PIL.Image as image
#导入数据处理库
import numpy as np

import jieba
df = pd.read_csv('./dataclean.csv',encoding='utf-8')
#设置value的显示长度为200，默认为50
pd.set_option('max_colwidth',200)
#显示所有列，把行显示设置成最大
pd.set_option('display.max_columns', None)
#显示所有行，把列显示设置成最大
pd.set_option('display.max_rows', None)

# print(df["标题"],file=open("weiboTansir.txt",'a+',encoding='utf-8'))


text_from_file_with_apath = open('weiboTansir.txt',encoding='utf-8').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# mask = np.array(image.open("./OIP-C.jpg"))
# mask = np.array(image.open(path.join(d,"./OIP-C.jpg")))
# the font from github: https://github.com/adobe-fonts
# wordcolud is not support the chinese font ,so we use the font on platform.
font = r'C:\Windows\Fonts\simfang.ttf'
my_wordcloud = WordCloud(max_words=100,
    collocations=False, background_color="white",
    font_path=font, width=1400, height=1400, 
    margin=10,random_state=1).generate(wl_space_split.lower())

# my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
my_wordcloud.to_file('tansirDaye.png')  # 把词云保存下来 