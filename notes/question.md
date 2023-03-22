# 面试题
## 要求：
以中文报告形式呈现分析结果（说明文字——图标），另外需要附代码

## 思路
平时做的是植物的，对应动物的数据接触的比较少。
首先，有个大概的认识[TCGA系列5-UCSC Xena网站的简单使用和数据下载-哔哩哔哩]()
>[TCGA系列5-UCSC Xena网站的简单使用和数据下载-哔哩哔哩](https://b23.tv/QXwE4oH)
-   如何确定TCGA-DD-AA3A-01编码含义

```txt
简而言之，编码机构BRS（Biospeciman Core Resource）根据来源机构（Tissue Source Site，TSS）和捐献者（Participation），给予编号TCGA-02 和 TCGA-02-0001，根据组织类型（Sample）如癌组织、正常组织等，编为TCGA-02-0001-01（01-09为癌组织，10-14为正常组织，组织类型编码详见https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/sample-type-codes）。同一种组织的标本又会被分装进不同容器（Vial），同一容器内又可分为多个小份（Portion），进一步编为 TCGA-02-0001-01B和TCGA-02-0001-01B-02。样品送至检测机构后，制备成不同的分析物（Analyte）检测，用不同字母编码，例如D表示DNA，R表示RNA。同一份分析物在检测过程中被加到检测板的某一加样孔中，分别编号 TCGA-02-0001-01B-02D-0182和TCGA-02-0001-01B-02D-0182-06。

```

>[组织类型编码](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/sample-type-codes)
>[TCGA条码](https://zhuanlan.zhihu.com/p/539346572)
-   临床数据如何确定
其他的大概涉及到梳理统计，选择什么工具
-   生产环境
>[online R clod](https://posit.cloud)
-   数据下载来源
>[dataset: gene expression RNAseq - IlluminaHiSeq](https://xenabrowser.net/datapages/?dataset=TCGA.LIHC.sampleMap%2FHiSeqV2&host=https%3A%2F%2Ftcga.xenahubs.net&removeHub=http%3A%2F%2F127.0.0.1%3A7222)
>[phenotype](https://xenabrowser.net/datapages/?cohort=TCGA%20Liver%20Cancer%20(LIHC)&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443)

### 试题：
1.从UCSC Xena数据库TCGA 肝癌转录组数据及临床信息
Transcriptome data and clinical information of hepatocellular carcinoma
```bash
1  wget -c  https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA.LIHC.sampleMap%2FLIHC_clinicalMatrix
2  wget -c https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA.LIHC.sampleMap%2FHiSeqV2.gz 
4  wget -c https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download/probeMap%2Fhugo_gencode_good_hg19_V24lift37_probemap 

```

```R
# version 02
rm(list = ls())
options(stringsAsFactors = F)

# 安装并载入所需的包
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

# BiocManager::install("edgeR")
library(edgeR)
# install.packages("SummarizedExperiment")
# BiocManager::install("locfit")
# BiocManager::install("DESeq2")
# install.packages("DESeq2")
# BiocManager::install("SummarizedExperiment",lib="/cloud/lib")
# library(DESeq2)


# BiocManager::install("DESeq2")

# 1. 数据预处理
data <- read.table("/fafu/jiangxiaojiao/data/TCGA.LIHC.sampleMap%2FHiSeqV2.gz",
                   header = TRUE, sep = "\t", row.names = 1)
data_clean <- na.omit(data) # 删除缺失值或空值

data_clinal <- read.table("/fafu/jiangxiaojiao/data/TCGA.LIHC.sampleMap%2FLIHC_clinicalMatrix", 
                                header = TRUE, sep = "\t", row.names = 1)
# data_clean_clinal <- na.omit(data_clinal)

# 获取患者的癌症状态
sample_id <- colnames(data_clean)
num <- as.numeric(substring(sample_id, 14, 15))  #截取字符串后转为数字
group_list = ifelse(num%in%1:9,"Tumor","Normal")  #ifelse实现分组

# 将 group_list 转换为只有一列的数据框
group_df <- as.data.frame(group_list)
group_df_clean <- na.omit(group_df)

# 在合并后的数据框中添加分组信息
df <- as.data.frame(sample_id)
df$Group <- ""
# 使用 substr 截取 A 列的最后 2 个字符
last_two_chars <- substr(df$A, nchar(df$A) - 1, nchar(df$A))

# 使用 ifelse 根据截取结果设置 B 列的值
df$Group <- ifelse(num%in%1:9,"Tumor","Normal")  #ifelse实现分组
# merged_data$Group <- ifelse(merged_data$Sample_Type == "Tumor", "disease", "normal")
# 将两个数据框按照 ID 列进行合并
# merged_df <- merge(sample_id, group_list)
# # 使用 ifelse 设置 B 中值的条件
# merged_df$y <- ifelse(df$A>0, TRUE, FALSE)

# 按照样品名以字母顺序排序
pheno <- pheno[order(rownames(pheno)), ]

# 将表型信息添加到矩阵中，并为每组分配分组信息
group <- factor(df$Group)
design <- model.matrix(~group)



# 查看 group_list 的类型
class(group_list)
class(data_clean)

# 创建 edgeR 对象
y <- DGEList(counts = data_clean, group = group)

# 进行基因过滤，按照要求选择出需要进行差异分析的基因
keep <- filterByExpr(y, design)
y <- y[keep,,keep.lib.sizes=FALSE]

# 规范化矩阵
y <- calcNormFactors(y)

# 估计离散度
y <- estimateDisp(y, design)

# 对规范化后的表达矩阵进行差异分析
fit <- glmQLFit(y, design)
qlf <- glmQLFTest(fit, coef=2)

# 筛选差异表达显著的基因
differentially_expressed_genes <- topTags(qlf, adjust.method = "BH", sort.by = "PValue", n = Inf)



```



## 数据的下载
通过R包UCSCXenaTools连接UCSC的XENA浏览器来探索TCGA等公共浏览器

>[生信专栏 | TCGA数据下载友好型——利用UCSC xena下载](https://zhuanlan.zhihu.com/p/539346572)
>[TCGA数据库的初次了解](https://www.jianshu.com/p/d662069a4a3d)
>[TCGA-LIHC](https://portal.gdc.cancer.gov/exploration?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.case_id%22%2C%22value%22%3A%5B%22109436aa-a655-429b-8d3b-1a43385c9016%22%2C%22146c5332-1af5-4c49-b740-9a9edc795f24%22%2C%224c960eee-e4b5-499d-a596-238aa78745a4%22%2C%226ed0b780-1b87-54ce-a036-8e74ece2a705%22%2C%229f056388-7529-4fd1-af11-c82cc350f51c%22%2C%22d884561b-5828-4c47-acd7-3f02e181b596%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LIHC%22%5D%7D%7D%5D%7D&searchTableTab=cases)

>[一文讲清TCGA数据库中样本编码信息](https://zhuanlan.zhihu.com/p/564801425)


2.对疾病和正常样本进行差异分析筛选出基因并进行差异分析
3.将差异基因与自噬基因取(需要自己去找自噬基因集)交集
4.利用交集基因构建多因素预后模型，画模型的ROC曲线。

## 参考文献
>[UCSC xena如何下载TCGA临床数据](https://zhuanlan.zhihu.com/p/113110843)

>[TCGA_BRCA数据挖掘测试](https://github.com/jmzeng1314/TCGA_BRCA)

>[An Integrated TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR) to drive high quality survival outcome analytics]()

>[利用R代码从UCSC XENA下载mRNA, lncRNA, miRNA表达数据并匹配临床信息](https://blog.csdn.net/qazplm12_3/article/details/114684113)