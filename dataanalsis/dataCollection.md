# 08 | 数据采集：如何自动化采集数据

    比如，量化投资，基于大数据预测未来股票的波动。

    我们需要通过多源的数据采集，收集到尽可能多的数据维度，
    同时保证数据的质量，这样才能得到高质量的数据挖掘结果。
-   数据源
![avatar](./../images/datasource.jpg)

    这四类数据源包括了：开放数据源、爬虫爬取、传感器和日志采集

-   开放数据源
    -   美国人口调查局
    -   除了政府、企业和高校也会开放相应的大数据，这方面北美相对来说做得好一些。
    -   国内，贵州做了大量的尝试，商务交通、旅游等
---
    很多研究是基于开放数据源的，所以就能比较其算法的好坏

-   爬虫
    -   特定网站的数据
-   传感器
    -   基本上采集的是物理信息
-   日志采集
    -   统计用户的操作

## 使用开放数据源
    从两个方面出发
    单位的维度
        行业的维度
如:
    ![avatar](./../images/linkopendata.jpg)

## 使用爬虫
    requests、Xpath、Pandas
    当然其他的，Scrapy 、Selenium、Phantom JS 等等啥的

    火车头采集器    老牌子啦
    八爪鱼          知名采集工具
    集搜客          完全可视化、无须编程

    云采集，很多时候通过切换IP以及云采集才是自动化采集的关键

## 日志采集
    运维人员的重要工作
    1.通过web服务器采集，如httpd、Nginx、tomcat都有
    2.自定义采集用户行为，用javascript监听用户的行为、AJAX异步请求后台记录日志等等

-   埋点
    -   就是在需要的位置采集相应的信息,进行上报
---
    市场上已经有第三方的工具,如友盟、Google Analysis、Talkingdata等。
    通过前端埋点的方式,然后在第三方工具里可以看到用户的行为数据。


    