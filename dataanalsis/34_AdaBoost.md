# 34丨AdaBoost - 分类的升华

AdaBoost的英文全称是Adaptive Boosting,中文含义是自适应提升算法。
它由Freund等人于1995年提出，是对Boosting算法的实现。

## 工作原理
Boosting算法是集成算法的一种，同时也是一类算法的总称。

这种强分类器是由一些弱分类器构成;

![avatar](./../images/adaBooost.png)

假设弱分类器为 Gi​(x)，它在强分类器中的权重 αi​，那么就可以得出强分类器 f(x)：
![avatar](./../images/adaBoost01.png)

那么问题就来了：
-   如何得到弱分类器，也就是在每次迭代训练的过程中，如何得到最优弱分类器？
-   弱分类器的权重是如何处理的？