
#1 比对
```bash
time /fafu/jiangxiaojiao/miniconda3/bin/bwa mem -t 4 -R '@RG\tID:foo\tPL:illumina\tSM:E.coli_K12' /fafu/jiangxiaojiao/201802_wgs_practice/input/E.coli/fasta/E.coli_K12_MG1655.fa /fafu/jiangxiaojiao/201802_wgs_practice/input/E.coli/fastq/SRR1770413_1.fastq.gz /fafu/jiangxiaojiao//201802_wgs_practice/input/E.coli/fastq/SRR1770413_2.fastq.gz | /fafu/jiangxiaojiao/miniconda3/bin/samtools view -Sb - > /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.bam && echo "** bwa mapping done **"
#2 排序

time /fafu/jiangxiaojiao/miniconda3/bin/samtools sort -@ 4 -m 4G -O bam -o  /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.sorted.bam  /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.bam && echo "** BAM sort done"rm -f  /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.bam

#3 标记PCR重复 到这一步了...
time ./gatk MarkDuplicates -I /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.sorted.bam -O /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.sorted.markdup.bam -M /fafu/jiangxiaojiao/201802_wgs_practice/output/E.coli/E_coli_K12.sorted.markdup_metrics.txt && echo "** markdup done **"#4 删除不必要文件(可选)
rm -f /201802_wgs_practice/output/E.coli/E_coli_K12.bam
rm -f /201802_wgs_practice/output/E.coli/E_coli_K12.sorted.bam

# echo export PATH="/fafu/jiangxiaojiao/biosoft/gatk:$PATH" >> ~/.bashrc
# export PATH="/fafu/jiangxiaojiao/biosoft/gatk/gradlew/:$PATH"

#5 创建比对索引文件
time /fafu/jiangxiaojiao/miniconda3/bin/samtools index /201802_wgs_practice/output/E.coli/E_coli_K12.sorted.markdup.bam && echo "** index done **"
```

<!-- #6 变异检测 -->
/fafu/jiangxiaojiao/miniconda3/bin/gatk CreateSequenceDictionary -R E.coli_K12_MG1655.fa -O E.coli_K12_MG1655.dict && echo "** dict done **"
<!-- 大概也得休息一下。。。 -->

#1 生成中间文件gvcf
time /fafu/jiangxiaojiao/miniconda3/bin/gatk HaplotypeCaller \
 -R ./input/E.coli/fasta/E.coli_K12_MG1655.fa \
 --emit-ref-confidence GVCF \
 -I ./output/E.coli/E_coli_K12.sorted.markdup.bam \
 -O ./output/E.coli/E_coli_K12.g.vcf && echo "** gvcf done **"

#2 通过gvcf检测变异
time /fafu/jiangxiaojiao/miniconda3/bin/gatk GenotypeGVCFs \
 -R ./input/E.coli/fasta/E.coli_K12_MG1655.fa \
 -V ./output/E.coli/E_coli_K12.g.vcf \
 -O ./output/E.coli/E_coli_K12.vcf && echo "** vcf done **"

## 变异检测需要很多的样本

很快我们就获得了E.coli K12这个样本初步的变异结果——E_coli_K12.vcf。之所以非要分成两个步骤，是因为我想借此告诉大家，变异检测不是一个样本的事情，有越多的同类样本放在一起joint calling结果将会越准确，而如果样本足够多的话，在低测序深度的情况下也同样可以获得完整并且准确的结果，而这样的分步方式是应对多样本的好方法。

最后，我们用bgzip对这个VCF进行压缩，并用tabix为它构建索引，方便以后的分析。

#1 压缩 
time /fafu/jiangxiaojiao/miniconda3/bin/bgzip -f ./output/E.coli/E_coli_K12.vcf

#2 构建tabix索引
time /fafu/jiangxiaojiao/miniconda3/bin/tabix -p vcf ./output/E.coli/E_coli_K12.vcf.gz
