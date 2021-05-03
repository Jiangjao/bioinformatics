bioconda，run
sh Miniconda3-latest-Linux-x86_64.sh

其他的安装

conda install bwa

Or a new environment can be created:

conda create -n aligners bwa bowtie hisat star

## 去除base界面
	
在打开终端的时候自动 执行了   conda  activate base 就会出现(base)

去掉（base) 输入 conda deactivate

原理，暂时不清楚。。。

## 软件包管理器
     软件包管理器是方便软件安装、卸载，解决软件依赖关系的重要工具。
      RedHat分支、
      windows也有软件包管理器，scoop，winget，chocolatey，推荐使用scoop
      rpm: Redhat Package Management；
      yum:Yellow dog Updater Modified ；
      apt：Advanced Packaging Tool；
     <li>Centos、RedHat使用yum包管理器，软件安装包格式rpm</li>
     <li>Debian、Ubuntu使用apt包管理器，软件安装包格式为deb</li>

### rpm 
      rpm 安装软件包处理依赖多，一个小版本的差异都不行。
-rpm 常见命令参数
	i,e(erase),q（query)

### yum
      相比于rpm解决了依赖的毛病；
      yum源在国外，嫌弃它慢，可以使用国内镜像。alibaba.com那边的。

####yum 配置文件
      -  /etc/yum.repos.d/CentOS-Base.repo
      - wget -O /etc/yum.repos.d/CentOS-Base.repo    http://mirrors.aliyun.com/repo/Centos-7.repo

### 二进制安装
-       源代码编译安装
       -     wget https://openresty.org/download/openresty-1.15.8.1.tar.gz
       -     tar -zxf openresty-VERSION.tar.gz              （解压 解包）
       -     cd openresty-VERSION/ 
       -     ./configure --prefix=/usr/local/openresty  （配置环境)
       -     make -j2                                                     (gcc 编译）
       -     make install
## 进程
      进程控制 && 进程的作业控制 && 进程之间的通信
### 进程管理
        程序运行调度的最小单位...
-       ./a.sh & 执行后台任务
-       jobs: 查看后台任务获取编号
-       fg 编号:调到前台
-       bg 编号:调到后台

        ctrl z 将进程挂起
        需要在同一个终端操作。nice 值控制进程获取资源的的级别。
### 守护进程
        nohup 与 & 配合使用。

### service
        其实所谓的服务管理工具就是封装了原本程序自己的启动，关闭，重启命令是么？
        作者回复: 好处是不用去记每个启动命令、参数及配置文件。
#### 基本使用
        cd /usr/lib/systemd/system
        vim sshd.service --查看服务文件
        cd /lib/systemd/system --服务文件目录
        ls -l runlevel*.target --查看服务文件映射

