# Transposable elements（转座子)
*A transposable element (TE, transposon, or jumping gene) is a **`DNA sequence`** that can change its position within a genome, sometimes creating or **`reversing mutations`** and **`altering the cell's genetic identity`** and **genome size**.
Transposition often results in duplication of the same genetic material. Barbara McClintock's discovery of them earned her a Nobel Prize in 1983.*


## classification
Two of the most abundant retrotransposon families in eukaryotes are
-   `LINE-1 (L1)`
-   `Bovine-B (BovB) `

转座子作为几种可动遗传因子之一，还可以根据其是`复制-粘贴`还是`剪切-粘贴`分为`I型转座子`和`II型转座子`两类[2]。

I型转座子

-   `反转录转座子`
    I型转座子转座`中间体`是`RNA`。I型转座子又被称为逆元件（Retro element）。该型转座子会先被转录为RNA，然后该RNA被逆转录，再次成为DNA，才被插入到目标位点中。

### Retrotransposon
>反转录转座子（Retrotransposon）是由`RNA介导`转座的转座子的元件，在`结构`和`复制`上与反转录病毒（retrovirus）类似，只是没有病毒感染必需的env基因。它通过`转录`合成mRNA，再`逆转录`合成新的元件整合到基因组中完成转座，每转座1次拷贝数就会增加1份，可以增强自己的基因组。
>因此，它是许多真核生物中数量最大的一类可活动遗传成分。在植物中特别丰富，它们是`核DNA`的一个主要组成部分。在玉米的基因组49-78％是反转录转座子，而在小麦中包含约90％的基因组重复序列和68％的转座子。在哺乳动物中，几乎有一半的基因组（45％至48％）包含转座子或残余转座子。人类基因组有大约42％反转录转座子，而DNA转座子约占2-3％。

反转录转座子与反座子 (retroposon) 较为相似，然而两者的主要区别为反转录转座子具有反转录酶，而反座子没有。

II型转座子

-   相比起I型转座子的“`复制后粘贴`”，II型转座子的转座行为就是“`剪切后粘贴`”。II型`转座中间体`是`DNA`，其实就是它本身。因此II型转座子又被称为不复制转座子。这类型的转座子在结构上有其特点。首先是转座子序列的两端，是两段正向重复序列（direct repeat，简称dR），与它们接壤的是反向重复序列（invert repeat，简为iR），就是所谓的“回文”序列。然后才是中间的插入序列（Insert sequence，简为IS）。

## 分析
>自然界中，转座子是含有转座酶基因的离散 DNA 片段，侧翼是含有转座酶结合位点的末端反向重复序列（TIR）。转座酶与 TIR 结合并从一个位置"切割"转座子并将其"粘贴"到新的位点（称为转座）。

## Long terminal repeat elements (LTR), which include retroposons
长末端重复序列（LTR）：反转录病毒的基因组的两端各有一个长末端重复序列(5’—LTR和3’—LTR)，不编码蛋白质，但含有启动子，增强子等调控元件，病毒基因组内的LTR可转移到细胞原癌基因邻近处，使这些原癌基因在LTR强启动子和增强子的作用下被激活，将正常细胞转化为癌细胞。

原文链接：https://blog.csdn.net/tanzuozhev/article/details/80958785

### 聚类分析
> OrthoMCL及orthofinder 两种软件进行聚类分析
### 共线性分析

对于亲缘关系较近的物种一般使用核苷酸序列来进行分析，如果在核苷酸水平不能呈现出很好的共线性的话，还可以换用编码基因水平的共线性（更适用于真核种）
除了全基因组共线性外，常见的还有功能基因簇的局部共线性分析
>https://www.jianshu.com/p/da5922df19d1
>http://www.cxyzjd.com/article/sinat_38163598/73180998

### 基因组Repeat Sequence
>Identifying repeats and transposable elements in sequenced genomes: how to find your way through the dense forest of programs

### 转座子分类的依据介绍
>https://zhuanlan.zhihu.com/p/183952007


病毒 自身的转座子有哪些。。

### 直系同源（orthology）和旁系同源（paralogy）

**`Orthologs`** 和 **`Paralogs`** 是同源序列的两种类型。**`Orthologs`** 描述在不同物种中来自于共同祖先的基因。**`Orthologs`** 基因可能有相同的功能，也可能没有。**`Paralogs`**描述在同一物种内由于基因复制而分离的同源基因。

***`Orthologs`*** 通常译作直系同源、直向同源、垂直同源。**`Paralogs`** 通常译作旁系同源、并系同源、横向同源。


[Xenology is the scientific study of extraterrestrial life. Derived from the Greek xenos, which as a substantive has the meaning "stranger, wanderer, refugee" and as an adjective "foreign, alien, strange, unusual."][1]

![avatar](./../images/Homology.png)

>Orthologs and Paralogs are two types of homologous sequences. Orthology describes genes in different species that derive from a common ancestor. Orthologous genes may or may not have the same function.Paralogy describes homologous genes within a single species that diverged by gene duplication.

>NCBI的Glossary中对paralog的定义是： A paralog is one of a set of homologous genes that have diverged from each other as a consequence of gene duplication. For example, the mouse a-globin andb-globin genes are paralogs. The relationship between mouse a-globin and chick b-globin is also considered paralogous (see the figure).

>NCBI的Glossary中对ortholog的定义是： Orthology describes genes in different species that derive from a single ancestral gene in the last common ancestor of the respective species.

>http://www.sciencedirect.com/science/article/pii/S0168952502027932

[1]: Henry George Liddell, Robert Scott, A Greek-English Lexicon, new (ninth) edition, with a supplement, Clarendon Press, Oxford, 1968.

