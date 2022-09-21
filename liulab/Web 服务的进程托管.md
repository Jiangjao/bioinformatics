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
3.Systemd

## 引用
>[Nohup](https://zh.wikipedia.org/zh-cn/Nohup)
>[Web 服务的进程托管](https://frostming.com/2020/05-24/process-management/)
>[关于 Markdown](https://zhuanlan.zhihu.com/p/28987530)