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

## 2.对疾病和正常样本进行差异分析筛选出基因并进行差异分析
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

percentage <- nrow(differentially_expressed_genes) / nrow(data_clean)

# 取交集
# 将differentially_expressed_genes转换为数据框对象
differentially_expressed_genes_name <- row.names(differentially_expressed_genes)
# differentially_expressed_genes_name <- as.data.frame()
autophagy_genes <- read.table("/fafu/jiangxiaojiao/methy_array/gene_temp.txt", header = FALSE)
# write.table(differentially_expressed_genes_name, file = "output.txt", sep = ",", row.names = FALSE)
vec2 <- as.vector(autophagy_genes[,])
result <- intersect(differentially_expressed_genes_name, vec2)

# 使用unique函数去除重复行
unique_result <- unique(result)

# 输出结果
unique_result

```



## 数据的下载
通过R包UCSCXenaTools连接UCSC的XENA浏览器来探索TCGA等公共浏览器

>[生信专栏 | TCGA数据下载友好型——利用UCSC xena下载](https://zhuanlan.zhihu.com/p/539346572)
>[TCGA数据库的初次了解](https://www.jianshu.com/p/d662069a4a3d)
>[TCGA-LIHC](https://portal.gdc.cancer.gov/exploration?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.case_id%22%2C%22value%22%3A%5B%22109436aa-a655-429b-8d3b-1a43385c9016%22%2C%22146c5332-1af5-4c49-b740-9a9edc795f24%22%2C%224c960eee-e4b5-499d-a596-238aa78745a4%22%2C%226ed0b780-1b87-54ce-a036-8e74ece2a705%22%2C%229f056388-7529-4fd1-af11-c82cc350f51c%22%2C%22d884561b-5828-4c47-acd7-3f02e181b596%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LIHC%22%5D%7D%7D%5D%7D&searchTableTab=cases)

>[一文讲清TCGA数据库中样本编码信息](https://zhuanlan.zhihu.com/p/564801425)



## 3.将差异基因与自噬基因取(需要自己去找自噬基因集)交集
自噬。Autophagy（自噬）来自于希腊语，是auto=self和phagy=phagein=to eat的结合。
您可以通过在公共数据库（如KEGG、GO等）中查找与自噬相关的基因集，然后将其与差异表达基因进行比较以找出它们的交集。以下是可能帮助您的示例代码：

```R
# 将自噬基因从文件中读入到 R 中，这里假设自噬基因的文件名为 "autophagy_genes.txt"
autophagy_genes <- read.table("autophagy_genes.txt", header=TRUE, stringsAsFactors=FALSE)
autophagy_genes <- autophagy_genes$GeneID

# 假设您已经得到了一组差异表达基因，以向量形式保存在 diff_expr_genes 变量中

# 找到交集
intersection <- intersect(diff_expr_genes, autophagy_genes)

# 输出结果
print(intersection)
```
在上面的代码中，我们首先将自噬基因从文件中读取到 R 中，并将其存储在向量 autophagy_genes中。然后，我们假设您已经得到了一组差异表达基因列表（以向量 diff_expr_genes 的形式给出），并使用 intersect() 函数找到它们与自噬基因列表中的交集。最后，我们将结果打印输出。请注意，在运行此代码之前，确保您已将差异表达基因和自噬基因的文件正确准备。
### 获取自噬基因
```python
# /usr/bin/python3
# -- encoding: utf-8 -

import requests
import functools
from bs4 import BeautifulSoup
import bs4

# 发送HTTP请求
url = "http://www.autophagy.lu/clustering/index.html"
response = requests.get(url)

# 解析HTML页面
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# 从第四个table开始
global flag
flag = True

def extract_table_data(table):
    """
    提取单个表格的数据

    table like this:


    <table width="100%">
        <tr>
            <td width="30%">
                <a href="http://www.lih.lu" style="border-color:white">
                    <img alt="LIH" height="" src="/Supplements/Pictures/public-research-center.png" style="border-color:white" title="LIH" width=""/>
                </a>
            </td>
            <td width="40%"></td>
            <td id="update_in_progress" style="border-color:red;text-align:right;font-size:12px" width="30%">
                <!--- marquee -->
                Update in progress
                <!---/marquee-->
            </td>
        </tr>
    </table>
    """


    soup = BeautifulSoup(str(table), 'html.parser')
    table = soup.table
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        print(row_data)
        load_into_file(row_data)

def load_into_file(line):
    # 去重不必要的字符
    line = [element.replace("\n", "").replace("\t","") for element in line]
    # line =  ','.join(str(line).split())
    
    # 由于tables是GeneId	Name	Symbol的结构（三个字符)
    # 起始字符GeneId是数字
    # 只需要判断line长度起码在3
    length = len(line)
    if length >=3:
        line_start = line[0]
        # 起始字符GeneId不是数字，舍弃
        if not line_start[:1].isdigit():
            return
        with open("./gene_temp.csv", mode="a+", encoding="utf-8") as f:
            f.write(",".join(line))
            f.write("\n")
        print("**** genes list ****")
        print(line[-1], file=open("./gene_temp.txt", mode="a+", encoding="utf-8"))
    # for element in line:
    #     print(element.strip(), file=open("./gene_temp.txt", mode="a+", encoding="utf-8"))
    #     print("\n")
# functools模块中的lru_cache装饰器来优化函数的性能。
# lru_cache装饰器会缓存函数的结果，并且在后续调用相同参数的函数时，直接返回缓存的结果，避免重复计算
@functools.lru_cache(maxsize=None)
def extract_all_tables(soup):
    """
    递归地提取所有表格的数据
    """
    all_data = []
    # if all_data == []:
    #     tables = soup.find_all('table')[:4]
    #     flag = False
    # else:
    tables = soup.find_all('table')
    valid_tables = []  # 保存有效的HTML标签对象
    for table in tables:
        if isinstance(table, bs4.element.Tag):  # 判断是否为HTML标签对象
            valid_tables.append(table)
    if valid_tables:
        # 第四个table
        for table in tables:
            # data = extract_table_data(table)
            # all_data.append(data)
            if len(table.find_all('table')) > 0:
                sub_soup = BeautifulSoup(str(table), 'html.parser')
                sub_data = extract_all_tables(sub_soup)
                # all_data += sub_data
            else:
                yield table
    # return all_data

# 解析HTML代码
# soup = BeautifulSoup(html, 'html.parser')

# 提取所有表格的数据
# tables = soup.find_all('table')[:3]
# tables = BeautifulSoup(str(tables), 'html.parser')
soup = BeautifulSoup(response.content, 'html.parser')
all_data = extract_all_tables(soup)

# print(all_data)
for table in all_data:
    # print(table)
    extract_table_data(table)
```

取交集
```R
percentage <- nrow(differentially_expressed_genes) / nrow(data_clean)

# 取交集
# 将differentially_expressed_genes转换为数据框对象
differentially_expressed_genes_name <- row.names(differentially_expressed_genes)
# differentially_expressed_genes_name <- as.data.frame()
autophagy_genes <- read.table("/fafu/jiangxiaojiao/methy_array/gene_temp.txt", header = FALSE)
# write.table(differentially_expressed_genes_name, file = "output.txt", sep = ",", row.names = FALSE)
vec2 <- as.vector(autophagy_genes[,])
result <- intersect(differentially_expressed_genes_name, vec2)

# 使用unique函数去除重复行
unique_result <- unique(result)

# 输出结果
unique_result
# [145] "ARNT"      "SESN2"     "DNAJB1"    "RAF1"      "EIF4EBP1"  "SIRT2"  
```
4.利用交集基因构建多因素预后模型，画模型的ROC曲线。

## 参考文献
>[UCSC xena如何下载TCGA临床数据](https://zhuanlan.zhihu.com/p/113110843)

>[TCGA_BRCA数据挖掘测试](https://github.com/jmzeng1314/TCGA_BRCA)

>[An Integrated TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR) to drive high quality survival outcome analytics]()

>[利用R代码从UCSC XENA下载mRNA, lncRNA, miRNA表达数据并匹配临床信息](https://blog.csdn.net/qazplm12_3/article/details/114684113)

>[自噬相关基因集合](https://zhuanlan.zhihu.com/p/560835923)

>[HADb Human Autophagy Database](http://www.autophagy.lu/index.html)