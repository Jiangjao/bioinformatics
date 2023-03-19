# 面试题
## 要求：
以中文报告形式呈现分析结果（说明文字——图标），另外需要附代码

## 思路
平时做的是植物的，对应动物的数据接触的比较少。
首先，有个大概的认识[TCGA系列5-UCSC Xena网站的简单使用和数据下载-哔哩哔哩]()
>[TCGA系列5-UCSC Xena网站的简单使用和数据下载-哔哩哔哩](https://b23.tv/QXwE4oH)
1. 那么有几个问题，如何确定TCGA-DD-AA3A-01编码含义，官网暂时没有找到
2. 临床数据如何确定

### 试题：
1.从UCSC Xena数据库TCGA 肝癌转录组数据及临床信息
Transcriptome data and clinical information of hepatocellular carcinoma

https://xenabrowser.net/datapages/?cohort=TCGA%20Liver%20Cancer%20(LIHC)&removeHub=http%3A%2F%2F127.0.0.1%3A7222

https://xenabrowser.net/datapages/?dataset=TCGA.LIHC.sampleMap%2FHiSeqV2&host=https%3A%2F%2Ftcga.xenahubs.net&removeHub=http%3A%2F%2F127.0.0.1%3A7222

```txt
简而言之，编码机构BRS（Biospeciman Core Resource）根据来源机构（Tissue Source Site，TSS）和捐献者（Participation），给予编号TCGA-02 和 TCGA-02-0001，根据组织类型（Sample）如癌组织、正常组织等，编为TCGA-02-0001-01（01-09为癌组织，10-14为正常组织，组织类型编码详见https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/sample-type-codes）。同一种组织的标本又会被分装进不同容器（Vial），同一容器内又可分为多个小份（Portion），进一步编为 TCGA-02-0001-01B和TCGA-02-0001-01B-02。样品送至检测机构后，制备成不同的分析物（Analyte）检测，用不同字母编码，例如D表示DNA，R表示RNA。同一份分析物在检测过程中被加到检测板的某一加样孔中，分别编号 TCGA-02-0001-01B-02D-0182和TCGA-02-0001-01B-02D-0182-06。

```
>[TCGA条码](https://zhuanlan.zhihu.com/p/539346572)

## 数据的下载
通过R包UCSCXenaTools连接UCSC的XENA浏览器来探索TCGA等公共浏览器

>[生信专栏 | TCGA数据下载友好型——利用UCSC xena下载](https://zhuanlan.zhihu.com/p/539346572)
>[TCGA数据库的初次了解](https://www.jianshu.com/p/d662069a4a3d)
>[TCGA-LIHC](https://portal.gdc.cancer.gov/exploration?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.case_id%22%2C%22value%22%3A%5B%22109436aa-a655-429b-8d3b-1a43385c9016%22%2C%22146c5332-1af5-4c49-b740-9a9edc795f24%22%2C%224c960eee-e4b5-499d-a596-238aa78745a4%22%2C%226ed0b780-1b87-54ce-a036-8e74ece2a705%22%2C%229f056388-7529-4fd1-af11-c82cc350f51c%22%2C%22d884561b-5828-4c47-acd7-3f02e181b596%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22TCGA%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.project_id%22%2C%22value%22%3A%5B%22TCGA-LIHC%22%5D%7D%7D%5D%7D&searchTableTab=cases)

>[一文讲清TCGA数据库中样本编码信息](https://zhuanlan.zhihu.com/p/564801425)

>[生信专栏 | TCGA数据下载友好型——利用UCSC xena下载](https://zhuanlan.zhihu.com/p/539346572)
2.对疾病和正常样本进行差异分析筛选出基因并进行差异分析
3.将差异基因与自噬基因取(需要自己去找自噬基因集)交集
4.利用交集基因构建多因素预后模型，画模型的ROC曲线。

## 参考文献
>[UCSC xena如何下载TCGA临床数据](https://zhuanlan.zhihu.com/p/113110843)

