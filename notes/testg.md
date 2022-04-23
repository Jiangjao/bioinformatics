todo:
1. 通过blast获得病毒的reads数目，具体过程要写一下


2. 参数
3. 具体需要自己写

4. 结果怎么写来着？ 这个好像很少，

```
# 各自对比到病毒，host上
<!-- 找到candidate sequences -->
# 然后把 candidate sequences 再次对比到host上, 找到序列
<!-- 缩小范围 -->
# 然后看一看，具体的在哪里

# 

cd ~/data/small_RNA数据及基因组重复测/测序数据/基因组重测序/Raw/FHV-csw/
nohup bowtie -q -a --strata --best -v 3 -p 30 --un Raw8-1Reads_unaligned02.fa --phred33-quals -x $HOME/data/reference/bowtie/BrownPlanthopper \
-1 E100007032_L01_639_1.fq.gz -2 E100007032_L01_639_2.fq.gz \
639.unique_BrownPlanthopper.bwt >>Raw.8-1.unique_summary 2>&1 & \

# 非病毒的探寻
nohup bowtie -q -a --strata --best -v 3 -p 30 --un filterFHVReads_unaligned02.fa --phred33-quals -x $HOME/data/reference/bowtie/FHVId/FHV \
-1 Raw8-1Reads_unaligned02_1.fa  -2 Raw8-1Reads_unaligned02_2.fa \
637.unique_FHV.bwt >>Raw.8-1.unique_summary 2>&1 & \

# 然后用blastn得到一部分的FHV片段
# 其实比对到FHV上，就可以啦
# 注意是否错配，有没有gap,错配长度等等。

nohup seqkit -j 30 fq2fa filterFHVReads_unaligned02_1.fa > filterFHVunaligned02_1.fa &

nohup seqkit -j 30 fq2fa filterFHVReads_unaligned02_2.fa > filterFHVunaligned02_2.fa &
# -e 100 -W 9 -F F -q -100 -g F, 其实这里是默认没有gap的
# 最小的长度是9吗，还是19呢？
blastn -query filterFHVunaligned02_1.fa -db $HOME/rna/test/reference/FHVvirus -outfmt ' 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send qseq sseq evalue bitscore' -task blastn-short -word_size 19 -evalue 100  -ungapped -penalty -100 -reward 1 -num_threads 30 > strandvirustest01.txt

blastn -query filterFHVunaligned02_2.fa -db $HOME/rna/test/reference/FHVvirus -outfmt ' 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send qseq sseq evalue bitscore' -task blastn-short -word_size 19 -evalue 100  -ungapped -penalty -100 -reward 1 -num_threads 30 > strandvirustest02.txt

```

```
File name	Description	microinjection	organism	Raw reads	size	Data type	Platform	Library
1	FHV-BPH-6dpi	        FHV	            BPH	        1_umi.fq.gz	
26	FHV-csw-6dpi	        FHV	            fly: csw	26_umi.fq.gz    


8	vFBPH-BPH-6dpi	        vDNA(FHV-BPH)	BPH	        8_umi.fq.gz	
8-1	vFBPH-BPH-6dpi	        vDNA(FHV-BPH)	BPH	        Raw.8-1.fq.gz 
28	vFBPH-csw-6dpi	        vDNA(FHV-BPH)	fly: csw	28_umi.fq.gz    


32	dsGFP-FHVΔB2-BPH-6dpi	FHVΔB2	        BPH	        32_umi.fq.gz 
33	dsA2-FHVΔB2-BPH-6dpi	FHVΔB2	        BPH	        33_umi.fq.gz    

2	RRSV-BPH-9dpi	        RRSV	        BPH	        2_umi.fq.gz	
5	vRRSV-BPH-6dpi	        vDNA(RRSV-BPH)	BPH	        5_umi.fq.gz	
5-1	vRRSV-BPH-6dpi	        vDNA(RRSV-BPH)	BPH	        Raw.5-1.fq.gz

10	RGDV-Rd-9dpi	        RGDV	        Rd	        10_umi.fq.gz




```


grep rna7.7_138225_14x Raw.8-1_final.txt
grep rna7.7_99990_19x Raw.8-1_final.txt