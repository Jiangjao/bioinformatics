# 转录组数据(Transcriptome data)练习01
>A transcriptome is the full range of messenger **`RNA`**, or **`mRNA`**, molecules expressed by an organism. The term "transcriptome" can also be used to describe the ***`array of mRNA transcripts`*** produced in a particular cell or tissue type.   
             --nature defination

由此可见，我们研究的更多的是RNA。

2013年，RNA-seq兴起，它 作为测量生物体转录组的首选方法，尽管仍然使用较旧的DNA微阵列技术。RNA-seq通过将长RNA转化为cDNA片段库来测量特定基因的转录。然后使用高通量测序技术对cDNA片段进行测序，并与参考基因组或转录组对齐，然后使用参考基因组或转录组创建基因的表达谱。

![avatar](./../images/Transicrip05.png)
当测序拼接好的高通量数据，可以上传到网上的各大数据中心NCBI（National Center for Biotechnology Information）、EBI（The European Bioinformatics Institute ）等等。


## 数据来源？
既然把数据传到了网上，那么就可以从数据库下载呗。
为了方便操作，我们以GSE149638这个为例子:
-  口口相传的NCBI,当年上课时就听说过这个，不妨试试
![avatar](./../images/tutorTranscrip.png)
![avatar](./../images/tutorTransm02.png)
- 2. 如果没有，可以问问百度百度呗。

## 获取Accession List

在NCBI中，原始数据被储存为`sra`（Sequence Read Archive）格式，把页面拉到最下方。
![avatar](./../images/tutorTransp03.png)
![avatar](./../images/tutorTranscrip08.png)
如果我点击Aceesion List 会下载一个文件，包含了序列号。
![avatar](./../images/tutorTransmp04.png)

## 正式下载
第一眼看到这么大的数据时，如果有个工具就好了。
NCBI自然是有的，sratoolkit
且看:
>https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software

### sra toolkit

```bash
## 建议在专用的 data 目录下
## 2021，06，21
## 记得查看环境变量中有没有这些工具的路径

# 自己的家目录哈
echo $HOME

mkdir -p  $HOME/rna/test/small_raw/
# 在 23.GSE149638 这个公共数据集里面是96个双端测序的转录组数据
# 注意，我把 SRR_Acc_list.txt放在这里，ヾ(￣▽￣)
cd  $HOME/project/23.GSE149638/raw
# 这一步，需要自己摸索摸索
cat ./SRR_Acc_List.txt | while read id
do
echo prefetch ${id} -O ./
done > downloadsra.sh

less downloadsra.sh
nohup bash downloadsra.sh &
```
![avatar](./../images/Transcrip03.png)

文件比较大，谨慎使用，这里为了方便演示，只下载了
SRR11652581
SRR11652582
SRR11652583
SRR11652584

![avatar](./../images/transcript04.png)
## 将SRA格式的数据转换为fastq格式
SRA数据库是用于存储二代测序的原始数据，这种数据格式不能直接进行处理，需要转换成fastq或fasta文件格式才能进行质控以及去adapt等处理。

SRA转fastq：
进行转换之前我们需要知道我们拿到的数据是单端还是双端数据，可以用fastq-dump -X 1 --split-spot SRRxxxxxxx.sra来判断测序类型.

```
fastq-dump -X 1 --split-spot -Z SRR11652581.sra | wc -l
```
如果返回值是4，就是单端SE；如果返回值是8，那么就是双端PE。

```bash
# 为了方便演示，就在当前文件夹下操作
# 查看文件内容，对每一个文件操作
cat ./SRR_Acc_List.txt | while read id
do
# 将sra文件转换成fastq
echo "fasterq-dump  --split-files -O ./ --outfile ${id}.fastq ${id}.sra"    # 这一步使用fastq-dump或fasterq-dump都可以

# pigz，压缩文件，功能类似gzip, 
echo "pigz -p 16 -f ./${id}_1.fastq"
echo "pigz -p 16 -f ./${id}_2.fastq"
done > sra2fq.sh

# 查看将要执行的文件内容
less sra2fq.sh
# 执行脚本
nohup bash sra2fq.sh &
```
我的文件如下:
![avatar](./../images/Transicrip06.png)
## 常见问题
1. preftech 下载很慢，有别的推荐吗？

Aspera试试呗；这篇文章有介绍
>[RNA-seq数据分析完全指北-01：数据下载](https://mp.weixin.qq.com/s?__biz=MzUzMTEwODk0Ng==&mid=2247496322&idx=2&sn=f9c78a63e8fd4d9f28b86d028d9c2f1c&chksm=fa4537bfcd32bea9417ef4766344019431743f90171f675c425b6ba0e81c91860e0d60ba88bc&scene=178&cur_album_id=1749887454125293572#rd)

2. 你的命令太复杂，我看不懂，比如read是什么意思。

的确，(⊙﹏⊙)，使用 man read瞅一瞅；
的确，比较复杂，写多了，就好些啦。

## 总结：
<!-- 这里该画张图，就可以啦，但是不清楚怎么画图 -->
## references
> Wang, Zhong; Gerstein, Mark; Snyder, Michael (January 2009). "RNA-Seq: a revolutionary tool for transcriptomics". Nature Reviews Genetics. 10 (1): 57–63. doi:10.1038/nrg2484. PMC 2949280. PMID 19015660.
> 
>[RNA-seq数据分析完全指北-01：数据下载](https://mp.weixin.qq.com/s?__biz=MzUzMTEwODk0Ng==&mid=2247496322&idx=2&sn=f9c78a63e8fd4d9f28b86d028d9c2f1c&chksm=fa4537bfcd32bea9417ef4766344019431743f90171f675c425b6ba0e81c91860e0d60ba88bc&scene=178&cur_album_id=1749887454125293572#rd)

>[NCBI sratoolskits](https://github.com/ncbi/sra-tools)
>