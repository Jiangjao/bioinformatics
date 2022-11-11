# Pro a problem
version 0.0.1
How to understand Figure 10 A？ 
![avatar](./../images/Figure%2010%20A.jpg)

>The Hapoltype and evolutionary analysis of OsNCED3. (A) Haplotype analysis in 5152 rice germplasm accessions. Orange indicates the reference (Nipponbare) allele sequence, **dark blue** indicates the     alternative allele sequence

## 过程
>Based on variations in the OsNCED3 promoter and coding ***sequences***, we identified 8 haplotypes with highest frequency variations across the OsNCED3 genome sequence (Figure 10A)
原文说我们依据的是测序数据，将它分为8个单倍型。
那么很容易想到，过程是啥呢？且看下文

### Haplotype and nucleotide diversity analysis
![avatar](./../images/Halotype%20and%20nucleotide%20diversity%20analysis.jpg)

1. snp-seek数据库下载数据看看
    1.1 里面有Phenotyped Data，数据量很大，
    1.2 原文的 table s3 | table s4也看了下
    >README 3K Rice Genomes  Permissive license This SNP , indel, and large SV dataset is released using the permissive license stated in The Toronto Statement from  the Toronto International Data Release Workshop Authors (Nature 461, 168-170(10 September 2009), doi:10.1038/461168a
    By downloading and using this dataset in part or in its entirety, you agree to abide to the spirit of the Toronto Statement.
2. 下载文件，用vcftools处理，需要筛选，
3. 处理后的文件，依据表型文件，依据the highest frequency .

比如这里的`references`的中例子:`通过vcf文件对基因进行单倍型分析`

通过例子，那么知道怎么来的，至于8个，就随它吧。


ps:其实它的species是7个
-   O. barthii
-   O.Glaberrima
-   O. longistaminata
-   O. nivara
-   O. meridionalis
-   O. rufipogon
-   O. sativa

## references

>[3K水稻SNP数据集的简单利用](https://blog.csdn.net/sinat_41244077/article/details/120337580)

>[Haplotype Analysis on RFGB](https://rmbreeding.cn/Genotype/haplotype)


>[download from snp-seek ](https://snp-seek.irri.org/_download.zul)

>[基于Vcf文件进行基因单倍型分析](https://www.jianshu.com/p/89e45a330de5)

>[单倍型分析技术研究进展 ](http://journals.im.ac.cn/html/cjbcn/2018/6/gc18060852.htm)

>[通过vcf文件对基因进行单倍型分析](https://gitee.com/zhangrenl/quickhapr)

>[GWAS分析-说人话（20）-单倍体关联分析](https://www.jianshu.com/p/66262b7655bc)

>[GWAS分析-说人话（14）- 如何查看SNP的基因型](https://www.jianshu.com/p/0afa963357de)