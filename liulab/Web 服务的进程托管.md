# Web 服务的进程托管
>**tag**: 入门级别:smile:
>>&emsp;&emsp;在web开发服务过程中（开发App, application),最后一步就是启动服务器。
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

**systemd**是Linux电脑系统之下的一套中央化系统（没看懂）及设置管理程序(init),包括守护进程、程序库以及应用软件，它由Lennart Poettering带头开发。其目标是提供更优秀的框架以表示系统服务间的依赖关系，并依此实现系统初始化时服务的并行启动，同时达到降低Shell的系统开销的效果，最终替代System V与BSD风格init程序。

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
```bash
# 先要赋予可读写的权限
systemctl enable test_blog
```

这样你的进程就自动加入开机自启动了，同样，systemd 也可以查看、启动、停止进程：

## 引用
>[Nohup](https://zh.wikipedia.org/zh-cn/Nohup)

>[Web 服务的进程托管](https://frostming.com/2020/05-24/process-management/)

>[关于 Markdown](https://zhuanlan.zhihu.com/p/28987530)

>[wiki systemd](https://zh.wikipedia.org/wiki/Systemd)


## share
:►/play flawless
:cherry_blossom:[weibo](https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F)
:sunflower:[telegram](https://telegram.org/)
:seedling:[zhihu](https://telegram.org/)