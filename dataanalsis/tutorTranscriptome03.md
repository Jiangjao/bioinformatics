# 转录组数据(Transcriptome data)练习03

### hisat 比对

```sh
cd ~/rna/test/cleanData

indexPrefix=/home/data/server/reference/index/hisat/hg38/genome 
ls *gz|cut -d"_" -f 1|sort -u |while read id;do
nohup  hisat2 -p 1 -x  $indexPrefix -1 ${id}*_1_val_1.fq.gz   -2 ${id}*_2_val_2.fq.gz  -S ${id}.hisat.sam & 
done 

# sam文件转bam
ls *.sam|while read id ;do (nohup samtools sort -O bam -@ 2   -o $(basename ${id} ".sam").bam   ${id}   & );done
# 这个过程会输出大量中间文件
rm *.sam 
# 为bam文件建立索引
ls *.bam |xargs -i samtools index {}
```

