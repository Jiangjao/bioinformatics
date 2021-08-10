# RNA-seq处理

## 1.数据质量
它是PCR扩增的，所以肯定有不合格的片段
多余 50% 会降低，数量质量的检控

## 2.illumicate 数据预处理，
其实去除接头，低质量片段
查看fastqc文件删除前面波动,
例如：trimmomatic 去除接头并去除低质量文件


## 3.mapping 与基因组进行比对
无论是histat2,bowtie的生成文件
文件一般有sam和bam,两者之间可以相互转换

一般在80%左右，来自线粒体或者叶绿体

---

## gene  experssion 表达分析（没做过）

1. 差异表达
gene?experssion
会得到count 文件

a 比b ---> a vs b vs c
差异表达分析文件

edg
PCA 
down(下降) ， up（上升) 表达


6.绘图
topgo.R  只能两两对比
以及topgo的升级版    多组对比
KEGG

7.gene_id 
查找gene，  sample_id 

一个基因对应多个id
1.bp
2.生物学过程
mp
分子功能
3cc
细胞组成

------


# small-RNA
50bp 测序
RNA 150bp 测序

## 检测
1. fast-qc检测质量


## 去接头，筛选mi-RNA
18-30bp的RNA进行分析的

绝对是有重复的，表达量很高
序列相同进行聚类,cluster
差异表达分析

## 特异性分析
质量控制
长度优势
24nt
探究其他问题；病毒处理
Base_length_distribution


### 病毒基因组
多组比对的结果
bam 转换成bed文件，覆盖情况和富集情况
通过R进行画图

## miRNA
mrocRNA靶位点的预测
psRNAtarget
tarfound
targetscand 

取交集得到最后的结果


流程
实验室自己的公共数据库?

·
网络上的数据库


tip:
    2021/08/09 只更新了RNA-seq处理的一般内容

> 关于RNA-seq; https://blog.csdn.net/qazplm12_3/article/details/102787318

> RNA-seq这十年; https://mp.weixin.qq.com/s/a3y46NNNO-wardO3XWwh0w