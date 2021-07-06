# 转录组数据(Transcriptome data)练习02

无论是数据，还是炒菜，对食材的掌控显得格外重要。
挑挑拣拣，祛伪存真，期待留下的是个究竟。



## 数据的样子
远看其形，近观其声，探个大概。无论其颜值是否在线，这次得看一看。

```bash
# 如果处理好了，瞅一瞅(oﾟvﾟ)ノ的序列
# 取2500条reads，文件太大了－O－
ls *gz|while read id ;do ( zcat $id  |head -10000 | gzip -c - >   $HOME/rna/test/small_raw/$id  );done 
cd $HOME/rna/test/small_raw/
```

## 数据清洗
测序的数据，是加了不少的标记(adpter),所以，要把这些东西去掉；
同时，有测到的，就有没有测到的，这些也得注意。
如果是双端测序，trim_galore命令需要加上--paired 的参数哦！

trim_galore是一个脚本，用于自动化质量控制和adpator修剪，并具有一些附加功能，用于移除RRBS序列文件的偏移甲基化位置（用于定向、非定向（或成对末端）测序。

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



