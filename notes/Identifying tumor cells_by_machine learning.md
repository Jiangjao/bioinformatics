<!--
 * @Author: jayjiao 918718278@qq.com
 * @Date: 2022-06-10 19:19:04
 * @LastEditors: jayjiao 918718278@qq.com
 * @LastEditTime: 2022-06-15 10:26:14
 * @FilePath: \geekbang\bioinformatics\notes\Identifying tumor cells_by_machine learning.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# test
we propose ikarus, a machine learning pipeline aimed at distinguishing tumor cells 
from normal cells at the single-cell level

consists of two steps: 
(1) discovery of a comprehensive tumor cell signature in the form of a gene set by consolidation of multiple expertly annotated single-cell datasets 

(2) training of a robust logistic regression classifer for stringent discrimination of tumor 
and normal cells followed by a network-based propagation of cell labels using a custom 
built cell–cell network

## noise
1. background noise
2. 
ikarus 

## env
 google colab
    滴滴云
    Kaggle
    极客云

## 配置
最高mem 达到58G 
fit model 的时候

GTX 1070 Ti 显存8G E5-2678 v3 24核 内存64G 220GB SSD + 6TB硬盘

### 预装环境
多框架组合环境 tensorflow1.15-pytorch1.7.0-opencv4.5-keras2.4.2.有图形界面
python 3.7， jupter

### error

```juptyer
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-38-446714ce6e01> in <module>
----> 1 _ = model.cnv_correct(cnv, ["tirosh"], save=True, name="tirosh")

KeyError: 'tirosh'adatas
```
需要查看对应的数据，并且data.preprocess_adata
2. model.fit 这一步很占用资源，可以按照tutorial 跳过

## references
[code](https://github.com/BIMSBbioinfo/ikarus)

[colab](https://colab.research.google.com/)

[scvi-tools](https://docs.scvi-tools.org/en/0.7.1/installation.html)