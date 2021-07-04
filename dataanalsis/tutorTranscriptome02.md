# 转录组数据(Transcriptome data)练习02

无论是数据，还是炒菜，对食材的掌控显得格外重要。
挑挑拣拣，祛伪存真，期待留下的是个究竟。



## 数据的样子
远看其形，近观其声，探个大概。无论其颜值是否在线，这次得看一看。

```bash
# 如果下载好了，瞅一瞅(oﾟvﾟ)ノ下载的序列
# 取2500条reads
ls *gz|while read id ;do ( zcat $id  |head -10000 | gzip -c - >   $HOME/rna/test/small_raw/$id  );done 
cd $HOME/rna/test/small_raw/
```

## 数据清洗
测序的数据，是加了不少的标记(adpter),所以，要把这些东西去掉；
同时，有测到的，就有没有测到的，这些也得注意。


```bash
cd  $HOME/rna/test/small_raw 
mkdir -p ../cleanData  
ls *gz|cut -d"_" -f 1|sort -u |while read id;do
nohup trim_galore -q 25 --phred33 --length 36 --stringency 3 --paired -o ../cleanData   ${id}*.gz & 
done 
```


