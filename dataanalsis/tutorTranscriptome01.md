# 转录组数据(Transcriptome data)练习
当做高通量数据分析时，常要从公共数据库如 NCBI、EBI 下载他人提交的高通量测序数据。

## 数据来源于哪门哪派？

为了方便操作，我们以GSE149638这个为例子
-  口口相传的NCBI,当年上课时就听说过这个，不妨试试
![avatar](./../images/tutorTranscrip.png)
![avatar](./../images/tutorTransm02.png)
- 2. 如果没有，可以问问百度百度呗。

## 获取Accession List

在NCBI中，原始数据被储存为sra格式，把页面拉到最下方。
![avatar](./../images/tutorTransp03.png)
如果我点击Aceesion List 会下载一个文件，包含了序列号。
![avatar](./../images/tutorTransmp04.png)

## 正式下载
第一眼看到这么多的数据时，想到emm，下载会很麻烦。如果有个工具就好了。
NCBI自然是有的，sra toolkit
且看:
>https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software

从NCBI上下载SRA原始数据，使用SRA TOOLKIT 进行下载和转化。
### sra toolkit

```
## 建议在专用的 data 目录下
## 2021，06，21
## 记得查看环境变量中有没有这些工具的路径

mkdir transcriptome
cd ./transcriptome/
cat ../SRR_Acc_List.txt | while read id
do
echo prefetch ${id} -O ./
done > prefetch.command

less prefetch.command
nohup bash prefetch.command &
```

## 将SRA格式转换为fastq格式


