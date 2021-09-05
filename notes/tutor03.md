### 双端序列去宿主

<!-- 先构建索引 -->
bowtie2

-t/--time  --un <path>        将unpaired reads写入到<path>.
--no-unal                     不能map到GENOME的reads,不保留sam记录
--un-conc <path>              不能map到GENOME的reads，fasta格式.
--un-conc-gz <path>           不能map到GENOME的reads，fasta格式, gzip压缩.
--al-conc <path>              能map到GENOME的reads，fasta格式.
--al-conc-gz <path>           能map到GENOME的reads，fasta格式, gzip压缩.
-p/--threads NTHREADS         设置线程数. Default: 1  如果你的计算机有多个CPU或者CPU内核，那么请使用-p参数。-p参数会让bowtie进入多线程模式。每一个线程都会使用单独的CPU或者CPU内核。这种并行的运算模式也会大大加快运算速度。


```bash
bowtie2 -p 10 -x /data/ref/bowtie2/mm10/mm10 -1 input_1.fq -2 input_2.fq | samtools sort -O bam -@ 10 -o - > output.bam


##双端测序数据去宿主：
bowtie2 --end-to-end --no-mixed --no-discordant --no-unal --sensitive --threads 30 \
-x $HOME/rna/test/reference/GCF \
-1 $HOME/data/small\ RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-S2/E100007032_L01_637_1.fq.gz \
-2 $HOME/data/small\ RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-S2/E100007032_L01_637_2.fq.gz \
--un-conc-gz E100007032_L01_637.clean.fastq.gz \

result

FHV-S2 有个寂寞


```

### 局部比对

```bash
bowtie2 --local -p 30 -x $HOME/rna/test/reference/FHV -1 $HOME/data/small\ RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-csw/E100007032_L01_637_1.fq.gz -2 $HOME/data/small\ RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-csw/E100007032_L01_637_2.fq.gz -S FHV-csw.sam
```

### 完整比对

```bash
bowtie2   --al-conc align -p 30 -x $HOME/rna/test/reference/FHV -1 $HOME/data/small\ RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-csw/E100007032_L01_637_1.fq.gz -2 $HOME/data/small\ RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-csw/E100007032_L01_637_2.fq.gz -S FHVwhole-csw.sam
```

没啥用呗

### a tricky play

ViralAligned_1.fastq
ViralAligned_2.fastq

<!-- 序列特征有哪些呢？？？？ -->
$HOME/rna/test/cleanData/test02/viral


