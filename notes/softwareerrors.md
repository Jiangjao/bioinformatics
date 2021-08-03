
## ITIS works not well
```bash
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 402M
-rw-r--r-- 1 root root 200M Aug  1 17:37 E100007032_L01_639_1.fq
-rw-r--r-- 1 root root 200M Aug  1 17:38 E100007032_L01_639_2.fq
drwxr-xr-x 2 root root 4.0K Aug  1 17:41 test.1627810863
drwxr-xr-x 2 root root 4.0K Aug  1 17:44 test.1627810905
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# cd test.1627810905/
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627810905]# ls
commands_rcd  FHV1.fa.sa                                  test.FHV1.informative.sam  test.ref_and_te.fa.pac
FHV1.fa       rds_te.fq1                                  test.ref_and_te.fa         test.ref_and_te.fa.sa
FHV1.fa.amb   rds_te.fq2                                  test.ref_and_te.fa.amb     test.ref_and_te.sam
FHV1.fa.ann   test.all_reads_aln_ref_and_te.sort.bam      test.ref_and_te.fa.ann     test.ref_and_te.sorted.bam
FHV1.fa.bwt   test.all_reads_aln_ref_and_te.sort.bam.bai  test.ref_and_te.fa.bwt     test.ref_and_te.sorted.bam.bai
FHV1.fa.pac   test.FHV1.empty                             test.ref_and_te.fa.list
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627810905]# ls -lh
total 378M
-rw-r--r-- 1 root root 1.6K Aug  1 17:44 commands_rcd
-rw-r--r-- 1 root root 3.2K Aug  1 17:44 FHV1.fa
-rw-r--r-- 1 root root    9 Aug  1 17:44 FHV1.fa.amb
-rw-r--r-- 1 root root   61 Aug  1 17:44 FHV1.fa.ann
-rw-r--r-- 1 root root 3.2K Aug  1 17:44 FHV1.fa.bwt
-rw-r--r-- 1 root root  778 Aug  1 17:44 FHV1.fa.pac
-rw-r--r-- 1 root root 1.6K Aug  1 17:44 FHV1.fa.sa
-rw-r--r-- 1 root root    0 Aug  1 17:44 rds_te.fq1
-rw-r--r-- 1 root root    0 Aug  1 17:44 rds_te.fq2
-rw-r--r-- 1 root root   92 Aug  1 17:44 test.all_reads_aln_ref_and_te.sort.bam
-rw-r--r-- 1 root root   16 Aug  1 17:44 test.all_reads_aln_ref_and_te.sort.bam.bai
-rw-r--r-- 1 root root    0 Aug  1 17:44 test.FHV1.empty
-rw-r--r-- 1 root root  56K Aug  1 17:44 test.FHV1.informative.sam
-rw-r--r-- 1 root root 138M Aug  1 17:41 test.ref_and_te.fa
-rw-r--r-- 1 root root 9.1K Aug  1 17:43 test.ref_and_te.fa.amb
-rw-r--r-- 1 root root  75K Aug  1 17:43 test.ref_and_te.fa.ann
-rw-r--r-- 1 root root 138M Aug  1 17:43 test.ref_and_te.fa.bwt
-rw-r--r-- 1 root root    0 Aug  1 17:41 test.ref_and_te.fa.list
-rw-r--r-- 1 root root  35M Aug  1 17:43 test.ref_and_te.fa.pac
-rw-r--r-- 1 root root  69M Aug  1 17:44 test.ref_and_te.fa.sa
-rw-r--r-- 1 root root  56K Aug  1 17:44 test.ref_and_te.sam
-rw-r--r-- 1 root root  22K Aug  1 17:44 test.ref_and_te.sorted.bam
-rw-r--r-- 1 root root  15K Aug  1 17:44 test.ref_and_te.sorted.bam.bai
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627810905]# cd ..
(base) [root@biocamp ~/rna/test/cleanData/test]# cd test.1627810863/
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627810863]# ls -lh
total 4.0K
-rw-r--r-- 1 root root 218 Aug  1 17:41 commands_rcd
-rw-r--r-- 1 root root   0 Aug  1 17:41 test.ref_and_te.fa.list
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627810863]# ls -lh
total 4.0K
-rw-r--r-- 1 root root 218 Aug  1 17:41 commands_rcd
-rw-r--r-- 1 root root   0 Aug  1 17:41 test.ref_and_te.fa.list
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627810863]# cd ..
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 402M
-rw-r--r-- 1 root root 200M Aug  1 17:37 E100007032_L01_639_1.fq
-rw-r--r-- 1 root root 200M Aug  1 17:38 E100007032_L01_639_2.fq
drwxr-xr-x 2 root root 4.0K Aug  1 17:41 test.1627810863
drwxr-xr-x 2 root root 4.0K Aug  1 17:44 test.1627810905
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# rm test.* -rf

(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 402M
-rw-r--r-- 1 root root 200M Aug  1 17:37 E100007032_L01_639_1.fq
-rw-r--r-- 1 root root 200M Aug  1 17:38 E100007032_L01_639_2.fq
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# ls *.fq.gz|while read id ;do ( zcat $id  |head -25000000 | gzip -c - >   $HOME/rna/test/cleanData/test/$id  );done ^C
(base) [root@biocamp ~/rna/test/cleanData/test]# cd
(base) [root@biocamp ~]# cd data/FHV-S
-bash: cd: data/FHV-S: No such file or directory
(base) [root@biocamp ~]# cd data/FHV-S2/
(base) [root@biocamp ~/data/FHV-S2]# ls
E100007032_L01_639_1.fq.gz  E100007032_L01_639_2.fq.gz
(base) [root@biocamp ~/data/FHV-S2]# ls *.fq.gz|while read id ;do ( zcat $id  |head -25000000 | gzip -c - >   $HOME/rna/test/cleanData/test/$id  );done
(base) [root@biocamp ~/data/FHV-S2]# cd $HOME/rna/test/cleanData/test/
(base) [root@biocamp ~/rna/test/cleanData/test]# ls
E100007032_L01_639_1.fq     E100007032_L01_639_2.fq     test639_1.fa
E100007032_L01_639_1.fq.gz  E100007032_L01_639_2.fq.gz  test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# gun *.zip

Command 'gun' not found, did you mean:

  command 'grn' from deb groff
  command 'grun' from deb grun
  command 'zun' from deb python-zunclient
  command 'zun' from deb python3-zunclient
  command 'gen' from deb multimon

Try: apt install <deb name>

(base) [root@biocamp ~/rna/test/cleanData/test]# gunzip *.zip
gzip: *.zip.gz: No such file or directory
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 1.7G
-rw-r--r-- 1 root root 200M Aug  1 17:37 E100007032_L01_639_1.fq
-rw-r--r-- 1 root root 641M Aug  1 17:51 E100007032_L01_639_1.fq.gz
-rw-r--r-- 1 root root 200M Aug  1 17:38 E100007032_L01_639_2.fq
-rw-r--r-- 1 root root 696M Aug  1 17:55 E100007032_L01_639_2.fq.gz
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# gunzip E100007032_L01_639_*
gzip: E100007032_L01_639_1.fq: unknown suffix -- ignored
gzip: E100007032_L01_639_1.fq already exists; do you wish to overwrite (y or n)? y
gzip: E100007032_L01_639_2.fq: unknown suffix -- ignored
gzip: E100007032_L01_639_2.fq already exists; do you wish to overwrite (y or n)? y
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 4.0G
-rw-r--r-- 1 root root 2.0G Aug  1 17:51 E100007032_L01_639_1.fq
-rw-r--r-- 1 root root 2.0G Aug  1 17:55 E100007032_L01_639_2.fq
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# mv E100007032_L01_639_1.fq  sample.fq1
(base) [root@biocamp ~/rna/test/cleanData/test]# mv E100007032_L01_639_2.fq sample.fq2
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 4.0G
-rw-r--r-- 1 root root 2.0G Aug  1 17:51 sample.fq1
-rw-r--r-- 1 root root 2.0G Aug  1 17:55 sample.fq2
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# perl /root/biosoft/ITIS/itis.pl -g $way/GCF.fna -t $way/FHV1.fa -l 500 -N test -1 sample.fq1 -2 sample.fq2 -e Y
Sunday, August 1, 2021: 18:19:53        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/mask_te_homo_in_genome.pl -g /root/rna/test/reference/GCF.fna -t /root/rna/test/reference/FHV1.fa  -o test.1627813193/test.ref_and_te.fa
CMD finished (7 seconds)
Sunday, August 1, 2021: 18:20:00        CMD: bwa index test.1627813193/test.ref_and_te.fa
[bwa_index] Pack FASTA... 1.14 sec
[bwa_index] Construct BWT for the packed sequence...
[BWTIncCreate] textLength=287458218, availableWord=32226252
[BWTIncConstructFromPacked] 10 iterations done. 53158778 characters processed.
[BWTIncConstructFromPacked] 20 iterations done. 98206858 characters processed.
[BWTIncConstructFromPacked] 30 iterations done. 138241642 characters processed.
[BWTIncConstructFromPacked] 40 iterations done. 173820650 characters processed.
[BWTIncConstructFromPacked] 50 iterations done. 205439306 characters processed.
[BWTIncConstructFromPacked] 60 iterations done. 233538042 characters processed.
[BWTIncConstructFromPacked] 70 iterations done. 258508250 characters processed.
[BWTIncConstructFromPacked] 80 iterations done. 280697786 characters processed.
[bwt_gen] Finished constructing BWT in 84 iterations.
[bwa_index] 102.55 seconds elapse.
[bwa_index] Update BWT... 0.96 sec
[bwa_index] Pack forward-only FASTA... 0.73 sec
[bwa_index] Construct SA from BWT and Occ... 54.15 sec
[main] Version: 0.7.7-r441
[main] CMD: bwa index test.1627813193/test.ref_and_te.fa
[main] Real time: 160.945 sec; CPU: 159.538 sec
CMD finished (161 seconds)
Sunday, August 1, 2021: 18:22:41        CMD: cp /root/rna/test/reference/FHV1.fa test.1627813193/
CMD finished (0 seconds)
Sunday, August 1, 2021: 18:22:41        CMD: bwa index test.1627813193/FHV1.fa
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.00 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.7-r441
[main] CMD: bwa index test.1627813193/FHV1.fa
[main] Real time: 0.013 sec; CPU: 0.003 sec
CMD finished (0 seconds)
Sunday, August 1, 2021: 18:22:41        CMD: bwa mem -T 20 -t 8 test.1627813193/test.ref_and_te.fa sample.fq1 sample.fq2 2>/dev/null | samtools view -@ 2 -buS - | samtools sort -@ 2 - test.1627813193/test.all_reads_aln_ref_and_te.sort
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 1871 sequences.
[bam_sort_core] merging from 10 files...
CMD finished (1704 seconds)
Sunday, August 1, 2021: 18:51:05        CMD: samtools index test.1627813193/test.all_reads_aln_ref_and_te.sort.bam
CMD finished (18 seconds)
Sunday, August 1, 2021: 18:51:23        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/lean_fq.pl -1 sample.fq1 -2 sample.fq2 -p test.1627813193/rds_te -i test.1627813193/FHV1.fa -c 8
[samopen] SAM header is present: 1 sequences.
CMD finished (256 seconds)
Sunday, August 1, 2021: 18:55:39        CMD: bwa mem -T 20 -v 1 -t 8 test.1627813193/test.ref_and_te.fa test.1627813193/rds_te.fq1 test.1627813193/rds_te.fq2 2>/dev/null  |tee  test.1627813193/test.ref_and_te.sam | samtools view -@ 2 -buS - | samtools sort -@ 2  - test.1627813193/test.ref_and_te.sorted
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 1871 sequences.
CMD finished (1 seconds)
Sunday, August 1, 2021: 18:55:40        CMD: samtools index test.1627813193/test.ref_and_te.sorted.bam
CMD finished (0 seconds)
Sunday, August 1, 2021: 18:55:40        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/extract_informative.pl -g /root/rna/test/reference/GCF.fna -s test.1627813193/test.ref_and_te.sam  -n FHV1 -p test.1627813193/test
CMD finished (2 seconds)
FHV1 no insertions
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 4.0G
-rw-r--r-- 1 root root 2.0G Aug  1 17:51 sample.fq1
-rw-r--r-- 1 root root 2.0G Aug  1 17:55 sample.fq2
drwxr-xr-x 2 root root 4.0K Aug  1 18:55 test.1627813193
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# cd test.1627813193/
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627813193]# ls -lh
total 1.6G
-rw-r--r-- 1 root root 1.6K Aug  1 18:55 commands_rcd
-rw-r--r-- 1 root root 3.2K Aug  1 18:22 FHV1.fa
-rw-r--r-- 1 root root    9 Aug  1 18:22 FHV1.fa.amb
-rw-r--r-- 1 root root   61 Aug  1 18:22 FHV1.fa.ann
-rw-r--r-- 1 root root 3.2K Aug  1 18:22 FHV1.fa.bwt
-rw-r--r-- 1 root root  778 Aug  1 18:22 FHV1.fa.pac
-rw-r--r-- 1 root root 1.6K Aug  1 18:22 FHV1.fa.sa
-rw-r--r-- 1 root root  360 Aug  1 18:55 rds_te.fq1
-rw-r--r-- 1 root root  360 Aug  1 18:55 rds_te.fq2
-rw-r--r-- 1 root root 1.2G Aug  1 18:51 test.all_reads_aln_ref_and_te.sort.bam
-rw-r--r-- 1 root root 531K Aug  1 18:51 test.all_reads_aln_ref_and_te.sort.bam.bai
-rw-r--r-- 1 root root    0 Aug  1 18:55 test.FHV1.empty
-rw-r--r-- 1 root root  56K Aug  1 18:55 test.FHV1.informative.sam
-rw-r--r-- 1 root root 138M Aug  1 18:20 test.ref_and_te.fa
-rw-r--r-- 1 root root 9.1K Aug  1 18:21 test.ref_and_te.fa.amb
-rw-r--r-- 1 root root  75K Aug  1 18:21 test.ref_and_te.fa.ann
-rw-r--r-- 1 root root 138M Aug  1 18:21 test.ref_and_te.fa.bwt
-rw-r--r-- 1 root root    0 Aug  1 18:19 test.ref_and_te.fa.list
-rw-r--r-- 1 root root  35M Aug  1 18:21 test.ref_and_te.fa.pac
-rw-r--r-- 1 root root  69M Aug  1 18:22 test.ref_and_te.fa.sa
-rw-r--r-- 1 root root  57K Aug  1 18:55 test.ref_and_te.sam
-rw-r--r-- 1 root root  22K Aug  1 18:55 test.ref_and_te.sorted.bam
-rw-r--r-- 1 root root  15K Aug  1 18:55 test.ref_and_te.sorted.bam.bai
(base) [root@biocamp ~/rna/test/cleanData/test/test.1627813193]# cd ..
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 4.0G
-rw-r--r-- 1 root root 2.0G Aug  1 17:51 sample.fq1
-rw-r--r-- 1 root root 2.0G Aug  1 17:55 sample.fq2
drwxr-xr-x 2 root root 4.0K Aug  1 18:55 test.1627813193
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# rm test.*
rm: cannot remove 'test.1627813193': Is a directory
(base) [root@biocamp ~/rna/test/cleanData/test]# rm test.* -rf
(base) [root@biocamp ~/rna/test/cleanData/test]# ls -lh
total 4.0G
-rw-r--r-- 1 root root 2.0G Aug  1 17:51 sample.fq1
-rw-r--r-- 1 root root 2.0G Aug  1 17:55 sample.fq2
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_1.fa
-rw-r--r-- 1 root root 1.1M Aug  1 15:43 test639_2.fa
(base) [root@biocamp ~/rna/test/cleanData/test]# perl /root/biosoft/ITIS/itis.pl -g $way/GCF.fna -t $way/FHV2.fa -l 500 -N test -1 sample.fq1 -2 sample.fq2 -e Y
Sunday, August 1, 2021: 19:03:32        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/mask_te_homo_in_genome.pl -g /root/rna/test/reference/GCF.fna -t /root/rna/test/reference/FHV2.fa  -o test.1627815812/test.ref_and_te.fa
CMD finished (8 seconds)
Sunday, August 1, 2021: 19:03:40        CMD: bwa index test.1627815812/test.ref_and_te.fa
[bwa_index] Pack FASTA... 1.16 sec
[bwa_index] Construct BWT for the packed sequence...
[BWTIncCreate] textLength=287454804, availableWord=32226016
[BWTIncConstructFromPacked] 10 iterations done. 53158404 characters processed.
[BWTIncConstructFromPacked] 20 iterations done. 98206148 characters processed.
[BWTIncConstructFromPacked] 30 iterations done. 138240644 characters processed.
[BWTIncConstructFromPacked] 40 iterations done. 173819380 characters processed.
[BWTIncConstructFromPacked] 50 iterations done. 205437828 characters processed.
[BWTIncConstructFromPacked] 60 iterations done. 233536356 characters processed.
[BWTIncConstructFromPacked] 70 iterations done. 258506340 characters processed.
[BWTIncConstructFromPacked] 80 iterations done. 280695716 characters processed.
[bwt_gen] Finished constructing BWT in 84 iterations.
[bwa_index] 102.27 seconds elapse.
[bwa_index] Update BWT... 0.97 sec
[bwa_index] Pack forward-only FASTA... 0.74 sec
[bwa_index] Construct SA from BWT and Occ... 53.88 sec
[main] Version: 0.7.7-r441
[main] CMD: bwa index test.1627815812/test.ref_and_te.fa
[main] Real time: 160.835 sec; CPU: 159.027 sec
CMD finished (161 seconds)
Sunday, August 1, 2021: 19:06:21        CMD: cp /root/rna/test/reference/FHV2.fa test.1627815812/
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:06:21        CMD: bwa index test.1627815812/FHV2.fa
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.00 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.7-r441
[main] CMD: bwa index test.1627815812/FHV2.fa
[main] Real time: 0.012 sec; CPU: 0.002 sec
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:06:21        CMD: bwa mem -T 20 -t 8 test.1627815812/test.ref_and_te.fa sample.fq1 sample.fq2 2>/dev/null | samtools view -@ 2 -buS - | samtools sort -@ 2 - test.1627815812/test.all_reads_aln_ref_and_te.sort
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 1871 sequences.
[bam_sort_core] merging from 10 files...
CMD finished (1710 seconds)
Sunday, August 1, 2021: 19:34:51        CMD: samtools index test.1627815812/test.all_reads_aln_ref_and_te.sort.bam
CMD finished (18 seconds)
Sunday, August 1, 2021: 19:35:09        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/lean_fq.pl -1 sample.fq1 -2 sample.fq2 -p test.1627815812/rds_te -i test.1627815812/FHV2.fa -c 8
[samopen] SAM header is present: 1 sequences.
CMD finished (241 seconds)
Sunday, August 1, 2021: 19:39:10        CMD: bwa mem -T 20 -v 1 -t 8 test.1627815812/test.ref_and_te.fa test.1627815812/rds_te.fq1 test.1627815812/rds_te.fq2 2>/dev/null  |tee  test.1627815812/test.ref_and_te.sam | samtools view -@ 2 -buS - | samtools sort -@ 2  - test.1627815812/test.ref_and_te.sorted
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 1871 sequences.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:39:10        CMD: samtools index test.1627815812/test.ref_and_te.sorted.bam
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:39:10        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/extract_informative.pl -g /root/rna/test/reference/GCF.fna -s test.1627815812/test.ref_and_te.sam  -n FHV2 -p test.1627815812/test
CMD finished (2 seconds)
FHV2 no insertions
(base) [root@biocamp ~/rna/test/cleanData/test]#
```

if it works well...

```bash
(base) [root@biocamp ~/biosoft/ITIS]# cd test_dir/
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# ls -lh
total 103M
-rwxrwxr-- 1 1034 1028  453 Oct 16  2014 mping.fa
-rwxrwx--- 1 1034 1028 2.0M Oct 16  2014 rice_chr1_200k.fa
-rw-r--r-- 1 root root  27M Aug  1 11:34 sample_data.tar.gz
-rwxrwx--- 1 1034 1028  38M Oct 23  2014 sample.fq1
-rwxrwx--- 1 1034 1028  38M Oct 23  2014 sample.fq2
drwxr-xr-x 2 root root  12K Aug  1 17:17 test.1627797474
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# perl path/to/itis.pl -g rice_chr1_200k.fa -t mping.fa -l 500 -N test -1 sample.fq1 -2 sample.fq2 -e Y
Can't open perl script "path/to/itis.pl": No such file or directory
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# perl ../itis.pl -g rice_chr1_200k.fa -t mping.fa -l 500 -N test -1 sample.fq1 -2 sample.fq2 -e Y
Sunday, August 1, 2021: 19:52:00        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/mask_te_homo_in_genome.pl -g rice_chr1_200k.fa -t mping.fa  -o test.1627818720/test.ref_and_te.fa
CMD finished (2 seconds)
Sunday, August 1, 2021: 19:52:02        CMD: bwa index test.1627818720/test.ref_and_te.fa
[bwa_index] Pack FASTA... 0.02 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.47 seconds elapse.
[bwa_index] Update BWT... 0.01 sec
[bwa_index] Pack forward-only FASTA... 0.01 sec
[bwa_index] Construct SA from BWT and Occ... 0.22 sec
[main] Version: 0.7.7-r441
[main] CMD: bwa index test.1627818720/test.ref_and_te.fa
[main] Real time: 0.767 sec; CPU: 0.733 sec
CMD finished (1 seconds)
Sunday, August 1, 2021: 19:52:03        CMD: cp mping.fa test.1627818720/
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:03        CMD: bwa index test.1627818720/mping.fa
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.00 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.7-r441
[main] CMD: bwa index test.1627818720/mping.fa
[main] Real time: 0.012 sec; CPU: 0.002 sec
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:03        CMD: bwa mem -T 20 -t 8 test.1627818720/test.ref_and_te.fa sample.fq1 sample.fq2 2>/dev/null | samtools view -@ 2 -buS - | samtools sort -@ 2 - test.1627818720/test.all_reads_aln_ref_and_te.sort
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 2 sequences.
CMD finished (11 seconds)
Sunday, August 1, 2021: 19:52:14        CMD: samtools index test.1627818720/test.all_reads_aln_ref_and_te.sort.bam
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:14        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/lean_fq.pl -1 sample.fq1 -2 sample.fq2 -p test.1627818720/rds_te -i test.1627818720/mping.fa -c 8
[samopen] SAM header is present: 1 sequences.
CMD finished (5 seconds)
Sunday, August 1, 2021: 19:52:19        CMD: bwa mem -T 20 -v 1 -t 8 test.1627818720/test.ref_and_te.fa test.1627818720/rds_te.fq1 test.1627818720/rds_te.fq2 2>/dev/null  |tee  test.1627818720/test.ref_and_te.sam | samtools view -@ 2 -buS - | samtools sort -@ 2  - test.1627818720/test.ref_and_te.sorted
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 2 sequences.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:19        CMD: samtools index test.1627818720/test.ref_and_te.sorted.bam
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:19        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/extract_informative.pl -g rice_chr1_200k.fa -s test.1627818720/test.ref_and_te.sam  -n mping -p test.1627818720/test
CMD finished (1 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/modify_informative.pl test.1627818720/test.mping.informative.sam > test.1627818720/test.mping.informative.full.sam
[samopen] SAM header is present: 2 sequences.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: samtools view -buS test.1627818720/test.mping.informative.sam | samtools sort - test.1627818720/test.mping.informative.sorted
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 2 sequences.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: samtools index test.1627818720/test.mping.informative.sorted.bam
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/te_realin_bwa.pl -n mping -s test.1627818720/test.mping.informative.full.sam -i test.1627818720/mping.fa -p test.1627818720/test
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/identity_inser_sites.pl -s test.1627818720/test.mping.informative.full.sam -g test.1627818720/test.ref_and_te.fa -l 500 -n mping -r test.1627818720/test.mping.alnte.sam -p test.1627818720/test -a 10
[samopen] SAM header is present: 1 sequences.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: samtools view -buS test.1627818720/test.mping.support.reads.sam | samtools sort - test.1627818720/test.mping.support.reads.sorted
[bam_header_read] EOF marker is absent. The input is probably truncated.
[samopen] SAM header is present: 2 sequences.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: samtools index   test.1627818720/test.mping.support.reads.sorted.bam
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: sort -k 3,3 -k 4,4n test.1627818720/test.mping.ins.loc.lst >test.1627818720/test.mping.ins.loc.sorted.lst
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:20        CMD: perl -I /root/biosoft/ITIS  /root/biosoft/ITIS/transform_to_bed.pl -b test.1627818720/test.all_reads_aln_ref_and_te.sort.bam -e test.1627818720/mping.fa -n mping -p test.1627818720/test.mping  -i test.1627818720/test.mping.ins.loc.sorted.lst -l 500  -w 250
Estimate the length of TSD is 3 bp
CMD finished (3 seconds)
Sunday, August 1, 2021: 19:52:23        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/filter_insertion.pl  -l test.1627818720/test.ref_and_te.fa.list -i test.1627818720/test.mping.raw.bed -n /t=3/TS=1/TE=1/ -q 1  -d 2,200 >test.1627818720/test.mping.filtered.bed
Smartmatch is experimental at /root/biosoft/ITIS/filter_insertion.pl line 99.
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:23        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/annotate_bed.pl -b test.1627818720/test.mping.filtered.bed   -g test.1627818720/test.ref_and_te.fa  -n mping -p test  -d test.1627818720
CMD finished (0 seconds)
Sunday, August 1, 2021: 19:52:23        CMD: perl -I /root/biosoft/ITIS /root/biosoft/ITIS/annotate_bed.pl -b test.1627818720/test.mping.filtered.bed   -g test.1627818720/test.ref_and_te.fa  -n mping -p test  -d test.1627818720
CMD finished (0 seconds)
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# ls- lh

Command 'ls-' not found, did you mean:

  command 'lsh' from deb lsh-client
  command 'ls' from deb coreutils
  command 'lsw' from deb suckless-tools
  command 'lsm' from deb lsm
  command 'lsc' from deb livescript

Try: apt install <deb name>

(base) [root@biocamp ~/biosoft/ITIS/test_dir]# ls
mping.fa  rice_chr1_200k.fa  sample_data.tar.gz  sample.fq1  sample.fq2  test.1627797474  test.1627818720
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# cd test.1627797474/
(base) [root@biocamp ~/biosoft/ITIS/test_dir/test.1627797474]# cd ..
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# ls -lh
total 103M
-rwxrwxr-- 1 1034 1028  453 Oct 16  2014 mping.fa
-rwxrwx--- 1 1034 1028 2.0M Oct 16  2014 rice_chr1_200k.fa
-rw-r--r-- 1 root root  27M Aug  1 11:34 sample_data.tar.gz
-rwxrwx--- 1 1034 1028  38M Oct 23  2014 sample.fq1
-rwxrwx--- 1 1034 1028  38M Oct 23  2014 sample.fq2
drwxr-xr-x 2 root root  12K Aug  1 17:17 test.1627797474
drwxr-xr-x 2 root root 4.0K Aug  1 19:52 test.1627818720
(base) [root@biocamp ~/biosoft/ITIS/test_dir]# cd test.1627797474/
(base) [root@biocamp ~/biosoft/ITIS/test_dir/test.1627797474]# ls -lh
total 34M
-rw-r--r-- 1 root root  3.6K Aug  1 13:58 commands_rcd
-rwxr-xr-- 1 root root   453 Aug  1 13:57 mping.fa
-rw-r--r-- 1 root root     8 Aug  1 13:57 mping.fa.amb
-rw-r--r-- 1 root root    34 Aug  1 13:57 mping.fa.ann
-rw-r--r-- 1 root root   512 Aug  1 13:57 mping.fa.bwt
-rw-r--r-- 1 root root   109 Aug  1 13:57 mping.fa.pac
-rw-r--r-- 1 root root   264 Aug  1 13:57 mping.fa.sa
-rw-r--r-- 1 root root 1000K Aug  1 13:58 rds_te.fq1
-rw-r--r-- 1 root root  998K Aug  1 13:58 rds_te.fq2
-rw-r--r-- 1 root root   23M Aug  1 13:58 test.all_reads_aln_ref_and_te.sort.bam
-rw-r--r-- 1 root root  6.0K Aug  1 13:58 test.all_reads_aln_ref_and_te.sort.bam.bai
-rw-r--r-- 1 root root   73K Aug  1 13:58 test.mping.alnte.sam
-rw-r--r-- 1 root root   96K Aug  1 13:58 test.mping.bg.sam
-rw-r--r-- 1 root root   678 Aug  1 13:58 test.mping.filtered.bed
-rw-r--r-- 1 root root   578 Aug  1 13:58 test.mping.igv.bat
-rw-r--r-- 1 root root  104K Aug  1 13:58 test.mping.informative.full.sam
-rw-r--r-- 1 root root   93K Aug  1 13:58 test.mping.informative.sam
-rw-r--r-- 1 root root   19K Aug  1 13:58 test.mping.informative.sorted.bam
-rw-r--r-- 1 root root  1.7K Aug  1 13:58 test.mping.informative.sorted.bam.bai
-rw-r--r-- 1 root root  5.4K Aug  1 13:58 test.mping.ins.loc.lst
-rw-r--r-- 1 root root  5.4K Aug  1 13:58 test.mping.ins.loc.sorted.lst
-rw-r--r-- 1 root root  2.7K Aug  1 13:58 test.mping.raw.bed
-rw-r--r-- 1 root root   51K Aug  1 13:58 test.mping.support.reads.sam
-rw-r--r-- 1 root root  7.2K Aug  1 13:58 test.mping.support.reads.sorted.bam
-rw-r--r-- 1 root root  1.5K Aug  1 13:58 test.mping.support.reads.sorted.bam.bai
-rw-r--r-- 1 root root   36K Aug  1 13:58 test.mping.unsupport.reads.sam
-rw-r--r-- 1 root root  2.0M Aug  1 13:57 test.ref_and_te.fa
-rw-r--r-- 1 root root    21 Aug  1 13:57 test.ref_and_te.fa.amb
-rw-r--r-- 1 root root    78 Aug  1 13:57 test.ref_and_te.fa.ann
-rw-r--r-- 1 root root  2.0M Aug  1 13:57 test.ref_and_te.fa.bwt
-rw-r--r-- 1 root root     0 Aug  1 13:57 test.ref_and_te.fa.list
-rw-r--r-- 1 root root  489K Aug  1 13:57 test.ref_and_te.fa.pac
-rw-r--r-- 1 root root  977K Aug  1 13:57 test.ref_and_te.fa.sa
-rw-r--r-- 1 root root  3.1M Aug  1 13:58 test.ref_and_te.sam
-rw-r--r-- 1 root root  318K Aug  1 13:58 test.ref_and_te.sorted.bam
-rw-r--r-- 1 root root  1.7K Aug  1 13:58 test.ref_and_te.sorted.bam.bai


```