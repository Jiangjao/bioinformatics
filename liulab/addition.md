# 补充
reference genome 待定
需要搭建流程，生产数据,eg：snakemake

## snp
    将snp 转换为json数据，
    然后将json数据字段存入数据库

snp 需要与对应的sample联系起来

找到其影响的代谢物变化，在不同tissue和sample中的变化、含量、注释信息。 根据SNP可以看出样品是杂合还是纯合，SNP和sample的关系，看出T/A等所占百分比，和相关测序信息，以及有无改变相关蛋白质序列。

## 转录组
-   输入基因，会查询到丰度、对热图、对应的sample, snp?
    - 替代方案
        - 或者使用特定的基因组浏览器，UCSC genome browser之类

## GWAS（需补充）
-   特定的基因组浏览器
    -   jbrowse-plugin-gwas
    -   替代方案:
        -   visualization
        -   web 端渲染，需要精通javascript, eg:D3.js

## reference:

>[snakemake 搭建流程](https://snakemake.readthedocs.io/en/stable/)

>DILINI DULANGIKA JATHUNGA DAHANAYAKE. 基于JSON的基因组突变数据处理关键技术研究[D].哈尔滨工业大学,2018.

>[vcf2json](https://github.com/bdolmo/vcf2json)

>[jbrowse-plugin-gwas](https://github.com/cmdcolin/jbrowse-plugin-gwas)

>[visualization](https://deck.gl/showcase)

>[api collection of KEGG、NCBI etc ](http://togows.org/)

>[GWAS tutorial](https://zhuanlan.zhihu.com/p/90414014)

>[easygwas](https://easygwas.ethz.ch/)

>[variation genome](https://api.ncbi.nlm.nih.gov/variation/v0/)

