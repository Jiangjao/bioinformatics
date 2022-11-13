# Pro a problem
version 0.0.2
How to understand Figure 10 A？
![avatar](./../images/Figure%2010%20A.jpg)

>The Hapoltype and evolutionary analysis of OsNCED3. (A) Haplotype analysis in 5152 rice germplasm accessions. Orange indicates the reference (Nipponbare) allele sequence, **dark blue** indicates the     alternative allele sequence

>[Haplotype](https://en.wikipedia.org/wiki/Haplotype)


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



## 基础概念
由于，西方科学建立在逻辑思维上面，逻辑思维基于各种概念。所以，趁这个机会，学习一下。
-   群体遗传结构（population genetic structure):指基因型在空间和时间上的分布形式，它包括群内的遗传遗传变异和种群的遗传分化。群体结构遗传是经过长时间的进化而形成的，很多物种的遗传结构反映了其进化历史中的特殊事件
-   群体结构中亚群的分类方法分为两种：基于距离和基于模型的方法。
    -   基于距离，通常会计算群体中每对个体的距离，以成对矩阵表示，并通过树形图或多维比例图呈现，但很难纳入其他信息（地理、表型信息）进行精确统计，人为确定亚群分类。
    -   基于模型的方法，通过假设每个亚群的观测值（如：基因频率）来自某个参数模型的随机抽样，使用统计（最大似然法或贝叶斯统计）对每个亚群成员和亚群模型参数进行推断，可以对群体进行精确聚类，检测群体内个体基因交流及混合程度。软件：STRUCTURE(Prithchard et al, 2000)
        -   可用FSTAT估计亚群分化固定系数、群体内分化系数（Fst)和群体遗传多样度(Hs)。对于大数据量的分析，可使用VCFtools、PopGenome等进行全基因组水平上群体分化相关参数计算。
        -   例如：水稻及其野化群体分析(引自Qiu et al, 2020)

-   自然选择的统计检验：
    -   自然选择：：正选择（positive selection)、负选择(净化选择negative selection)和平衡选择(balacing selection)，平衡选择在多数情况下会倾向维持群体的遗传多样性
    -   中性检验是判断群体进化一个方法：
        -   以中性进化学说作为零假设，通过统计检验的方法，检测一个群体的遗传参数是否符合中性进化模型。
        -   大体分为两类:基于种类多态性（intraspecific polymorphism)的检验方法、
    -   基于位点变异频率分布
        -   Tajima's D检验
        -   Fu & Li's D和F检验


>[单倍型组装与推断](http://doc.aporc.org/attach/Course001/Bioinformatics-3.pdf)

>[杨少滢,缪立生,肖成,刘宇,沈宏旭,吴健,高青山,赵玉民,曹阳.沃金黑牛FGF14基因单倍型与生长性状的相关性分析[J/OL].中国畜牧杂志:1-10[2022-11-13].DOI:10.19556/j.0258-7033.20220630-02.](https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CAPJ&dbname=CAPJLAST&filename=ZGXM20221103001&uniplatform=OVERSEA&v=_qqq1X2svHerNGtKoHmuhxQcfEjGEfOT0foOyQEXgkR_M5xTnlxJbLNs8w1YlWAB)