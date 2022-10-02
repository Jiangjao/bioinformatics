# emm
version 0.1.1, by xiaojiao
<!-- 然后NAR文章的部分初稿我已经写好了，还是要细化所有的数据处理和功能的内容

-   对，有博士水准
-   是，你参考他的架构就行，比如：他做的是代谢组学数据库优化，他提出了可能存在的问题，做了优化，一个优化他做的是一个数据库
-   但是比如说，你提出茶叶数据库的问题，如何解决，然后你的体量是一个数据库 -->

## feature
1. Browse GWAS locus for single trait within given region. If not specified, the region with the **most significant P-value** was displayed. The scatter plot region can be easily changed by clicking a bar in the overview navigational Manhattan Plot panel. You could also search the GWAS data through our Jbrowser2.

2. Web services:download data used by RESTful web-service
>比如这个[`api collection of KEGG、NCBI etc `](http://togows.org/)

-   We defined a set of `RESTful web-service` calls for internal use and shared to collaborators through our development site.Some data calls may require login or limitation of times of downloads.Also, you can contact us.
-   这个只是方便了下载
-   下载功能还没有实现


>>[RESTful web-service](https://en.wikipedia.org/wiki/Representational_state_transfer)

1. data source collected from NC & EBI
>[`Metabolite signatures of diverse Camellia sinensis tea populations`](https://www.nature.com/articles/s41467-020-19441-1)

## 参考
>[ZEAMAP](http://www.zeamap.com/resource/genetics)

>[Rice SNP-seek database update: new SNPs, indels, and queries ](https://academic.oup.com/nar/article/45/D1/D1075/2605752)

>[data on EBI](https://www.ebi.ac.uk/metabolights/MTBLS1405)

>[data source ](https://www.nature.com/articles/s41467-020-19441-1)

>[api collection of KEGG、NCBI etc ](http://togows.org/)
