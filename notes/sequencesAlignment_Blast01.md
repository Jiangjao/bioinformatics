# 序列对比-本地Blast使用初探
    本地BLAST是NCBI向用户提供的在计算机本地，对核酸、蛋白序列进行局部比对的算法工具

>优缺点：本地BLAST具有可自建比对库、定义输出信息格式、无需连接网络等优点，但需要输入命令行，不如在线BLAST便捷

其实用`biopython` 也可以达到同样的效果

## 运行命令行BLAST

### blast软件下载
    conda install blast..
    or
    NCBI下载

tips:暂无
    程序的输入文件是query序列（- i参数）而和库文件（-d 参数），比对类型的选择（- p参数）和输出文件（- o 参数）由用户指定。其中“-p”参数有5中取值：

-p blastp：蛋白序列与蛋白库做比对。

-p blastx：核酸序列对蛋白库的比对。

-p blastn：核酸序列对核酸库的比对。

-p tblastn：蛋白序列对核酸库的比对。

-p tblastx：核酸序列对核酸库在蛋白级别的比对

### Genome下载
    以Oryza sativa为例，wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/433/935/GCF_001433935.1_IRGSP-1.0/

    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/433/935/GCF_001433935.1_IRGSP-1.0/GCF_001433935.1_IRGSP-1.0_genomic.fna.gz
    下载一个病毒的，怎么下的呢，忘了。GCF_000850725.1_ViralMultiSegProj14797_genomic.fna

### 解压
    gunzip GCF_001433935.1_IRGSP-1.0_genomic.fna.gz

### 创建库

#Create BLAST database  using an existing BLAST database or FASTA sequence file as input
```c
makeblastdb -in GCF_001433935.1_IRGSP-1.0_genomic.fan -dbtype prot
```
#### Result
```c
Building a new DB, current time: 05/05/2021 17:06:25
New DB name:   /fafu/jiangxiaojiao/data/GCF_001433935.1_IRGSP-1.0_genomic.fna
New DB title:  GCF_001433935.1_IRGSP-1.0_genomic.fna
Sequence type: Nucleotide
Keep MBits: T
Maximum file size: 1000000000B
Adding sequences from FASTA; added 58 sequences in 3.7626 seconds.
```

当需要进行大量比对的时候，将BLAST数据库本地化能极大提高效率。

创建一个本地水稻数据库,这是通过调用BLAST的makeblastdb来实现的。
    
    makeblastdb -in zebrafish.1.protein.faa -dbtype nucl

#### 序列和库的局部比对
分别对应:工具 -query 比对序列文件(fasta格式) -db 数据库名 -out 比对结果文件名 -evalue 期望值(默认为10，一般设置le-5) -outfmt 比对结果参数

#### 准备开始了哈
接下来，我们调用BLAST进行搜索：

blastn -query  GCF_000850725.1_ViralMultiSegProj14797_genomic.fna  -db GCF_001433935.1_IRGSP-1.0_genomic.fna -out RiceVirus_GCF_001433935-first.x.Rice——dwarf_virus.tsv -outfmt 6 -evalue 1e-5 -max_hsps 100 

#blastn: 调用核酸序列比对 -query 比对序列文件(fasta格式) -db 数据库名 -out 比对结果文件名 -evalue 期望值(默认为10，一般设置le-5) -outfmt 比对结果的输出参数：0-18，常用0,5,6,7

#### 比对结果的输出参数：0-18，常用0,5,6,7

- 0：成对输出，与在线比对结果相同
- 5：输出XML格式
- 6：输出table格式
- 7：输出带有注释行的table格式，有以下参数可通过’’7 参数’’的形式接在-outfmt后使用：
-----
- qacc：查询基因的序列号
- sacc：库基因的序列号
- qstart：查询基因的匹配开始位置
- sstart：库基因的匹配开始位置
- qend：查询基因的匹配结束位置
- send：库基因的匹配结束位置
- qseq：查询基因的匹配序列
- sseq：库基因的匹配序列
- evalue：期望值
- bitscore：比特得分还是每对得分？(这个没用过)
- score：原始得分
- length：对齐长度
- pident：相同匹配百分比
- nident：相同匹配数量
- mismatch：不匹配数量
- gaps：间隙数
- gapopen：间隙开口数
- positive：积极得分的个数
- ppos：积极得分的百分比

##  搭建网页BLAST
曾经的BLAST安装后提供wwwblast用于构建本地的BLAST网页工具，但是BLAST+没有提供这个工具，好在BLAST足够出名，也就有人给它开发网页版工具。如viroBLAST和Sequenceserver, 目前来看似乎后者更受人欢迎。

暂且放过它吧.

作者：xuzhougeng
链接：https://www.jianshu.com/p/de28be1a3bea
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

### References
>[BLAST实操|Linux 本地序列比对](https://zhuanlan.zhihu.com/p/269565747)


>[《BLAST Command Line Applications User Manual》](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs)

>[Bioinformatics Sequence and Genome Analysis](http://www.bioinformaticsonline.org/)

>[ 实验生信那些事儿](https://zhuanlan.zhihu.com/p/65505346)

>[BLASTn output format 6](http://www.metagenomics.wiki/tools/blast/blastn-output-format-6)