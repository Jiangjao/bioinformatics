# Web 服务的进程托管
>**tag**: 入门级别:smile:
>>&emsp;&emsp;在web开发服务过程中（开发App, application),最后一步就是启动服务器。<br>
如何让应用长时间运行？在大部分的教程中一般使用uwsgi或者gunicorn。运行过后，会占用终端对话，进入[`长对话`](#code)模式

```bash
[2020-05-23 22:54:57 +0800] [13077] [INFO] Starting gunicorn 20.0.4
[2020-05-23 22:54:57 +0800] [13077] [INFO] Listening at: unix:/tmp/***.socket (13077)
[2020-05-23 22:54:57 +0800] [13077] [INFO] Using worker: sync
[2020-05-23 22:54:57 +0800] [13084] [INFO] Booting worker with pid: 13084
```

## Nohup
2.Supervisor

## Systemd
&emsp;&emsp;[`systemd`](https://zh.wikipedia.org/wiki/Systemd),名字源于Unix中的一个惯例:在Unix中
常以"d"作为系统守护进程(daemon,也称作后台进程)的后缀标识。:relieved:

**systemd**是Linux电脑系统之下的一套中央化系统（没看懂）及设置管理程序(init),包括守护进程、程序库以及应用软件，它由Lennart Poettering带头开发。<br>&emsp;&emsp;其目标是提供更优秀的框架以表示系统服务间的依赖关系，并依此实现系统初始化时服务的并行启动，同时达到降低Shell的系统开销的效果，最终替代System V与BSD风格init程序。

```bash
[Unit]
Description=My blog service

[Service]
Type=forking
ExecStart=gunicorn -b :8888 -w 4 my_blog.wsgi
KillMode=process
Restart=on-failure
RestartSec=3s

[Install]
WantedBy=multi-user.target
```

保存到[`/etc/systemd/system/test_blog.service`](#Systemd)。然后执行：


<!-- ###### bash脚本的service服务 ######
```bash
[Unit]
Description=JBrowse service

[Service]
Type=simple
ExecStart=/var/www/watchApplication.sh
KillMode=process
Restart=on-failure
RestartSec=3s

[Install]
WantedBy=multi-user.target
``` 
-->


```bash
# 先要赋予可读写的权限
systemctl enable test_blog
```

这样你的进程就自动加入开机自启动了，同样，systemd 也可以查看、启动、停止进程：

```bash
systemctl status test_blog    # 查看进程状态
systemctl stop test_blog    # 终止my_blog进程
systemctl start test_blog    # 启动my_blog进程
systemctl restart test_blog    # 重新启动my_blog进程
```
## 大量小文件的存储场景，有什么优化办法？
其实是要实现的是**中小型分布式文件系统管理**
fasthdfs?
PostgreSQL似乎可以
api-->PostgREST
好像就是这样子的

## HDFS 配置与使用
之前提到过的 Hadoop 三种模式：单机模式、伪集群模式和集群模式。

-   单机模式：Hadoop 仅作为库存在，可以在单计算机上执行 MapReduce 任务，仅用于开发者搭建学习和试验环境。
-   伪集群模式：此模式 Hadoop 将以守护进程的形式在单机运行，一般用于开发者搭建学习和试验环境。
-   集群模式：此模式是 Hadoop 的生产环境模式，也就是说这才是 Hadoop 真正使用的模式，用于提供生产级服务。


## Tripal 的使用

## 引用
>[Nohup](https://zh.wikipedia.org/zh-cn/Nohup)

>[Web 服务的进程托管](https://frostming.com/2020/05-24/process-management/)

>[关于 Markdown](https://zhuanlan.zhihu.com/p/28987530)

>[wiki systemd](https://zh.wikipedia.org/wiki/Systemd)

>[Linux 利用systemd开机自启shell脚本](https://blog.csdn.net/qq_41539778/article/details/109361023)

>[fullstackpython](https://www.fullstackpython.com/table-of-contents.html)

>[大量小文件的存储场景，有什么优化办法？](https://www.zhihu.com/question/26504749)

>[HDFS海量小文件存储方案](https://zhuanlan.zhihu.com/p/363478313)

>[HDFS 配置与使用](https://www.runoob.com/w3cnote/hdfs-setup.html)


## share
:►/play flawless
:cherry_blossom:[weibo](https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F)
:sunflower:[telegram](https://telegram.org/)
:seedling:[zhihu](https://telegram.org/)