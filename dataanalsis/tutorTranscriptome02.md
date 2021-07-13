# 转录组数据(Transcriptome data)练习02

无论是数据，还是炒菜，对食材的掌控显得格外重要。
挑挑拣拣，祛伪存真，期待留下的是个究竟。



## 数据的样子
远看其形，近观其声，探个大概。无论其颜值是否在线，这次得看一看。

```bash
# 注意，此时在 $HOME/project/23.GSE149638/raw目录下

# 如果处理好了，瞅一瞅(oﾟvﾟ)ノ的序列
# 可以取一定长度的reads，试一试，毕竟文件太大了－O－
ls *gz|while read id ;do ( zcat $id   | gzip -c - >   $HOME/rna/test/small_raw/$id  );done 
cd $HOME/rna/test/small_raw/
```

## 数据清洗
测序的数据，是加了不少的标记(adpter),所以，要把这些东西去掉；
同时，有测到的，就有没有测到的，这些也得注意。
如果是双端测序，trim_galore命令需要加上--paired 的参数哦！

Trim Galore是对FastQC和Cutadapt的包装。它适用于所有高通量测序，包括RRBS(Reduced Representation Bisulfite-Seq ), Illumina、Nextera 和smallRNA测序平台的双端和单端数据的软件。主要功能包括两步：
第一步首先去除低质量碱基，然后去除3' 末端的adapter, 如果没有指定具体的adapter，程序会自动检测前1million的序列，然后对比前12-13bp的序列是否符合以下类型的adapter
- Illumina: AGATCGGAAGAGC
- Small RNA: TGGAATTCTCGG
- Nextera: CTGTCTCTTATA


```bash
cd  $HOME/rna/test/small_raw 
# 在上一级，创建新文件夹
mkdir -p ../cleanData  
# 小文件先试试呗
ls *gz|cut -d"_" -f 1|sort -u |while read id;do
nohup trim_galore -q 25 --phred33 --length 36 --stringency 3 --paired -o ../cleanData   ${id}*.gz & 
done 
```

```bash
# 如果是单端 ： 
ls *gz| sort -u |while read id;do
echo trim_galore -q 25 --phred33 --length 36 --stringency 3   -o ../cleanData   ${id} 
done   > trim_galore.sh 
```

全部的 trim_galore 命令运行完毕后，得到的clean的fq文件如下:



>http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/

>[Trim Galore User Guide](13_datatransform.mdhttps://github.com/FelixKrueger/TrimGalore/blob/master/Docs/Trim_Galore_User_Guide.md)
