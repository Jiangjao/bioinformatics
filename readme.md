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

#### yum 配置文件
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


## 57 | Shell 脚本的格式
    UNIX的哲学：一条命令只做一件事
	为了组合命令和多次执行，使用脚本文件来保存需要执行的命令
	赋予该文件执行权限(chmod u+rx filename)

## 58 | Shell脚本不同执行方式的影响

### 执行命令
     bash ./filename.sh
     ./filename.sh
     source ./filename.sh
     .filename.sh

### 内建命令和外部命令
    可以用type 来查看
<ul>
<li>内建命令不需要创建子进程</li>
<li>内部命令对当前Shell生效</li>
</ul>
source ./filename.sh 与.filename.sh 是一样滴。都会在当前进程下。
而bash ./filename ./filename.sh 会产生子进程。
## 63 | 环境变量、预定义变量与位置变量
	env      查看环境变量
	$PATH 
### 预定义变量
	$?       上一条命令是否执行成功(suceessful 0)
	$$       可以显示当前进程PID    一般用来检测脚本检测or运行状态
	$0		 当前进程名称

#### 位置变量
	执行shell脚本的时候，可以为shell脚本带上更多的参数

## 60 | 重定向符号
-	一个进程默认会打开标准输入、标准输出、错误输出三个文件描述符
-	输入重定向符号 " <"
	-	read var </path/to/file
-	输出重定向符号 ">"   ">>"   "2>"   "&>"
	-	echo 123 > /path/to/a/file
-	输入和输出重定向组合使用
	-	cat > /path/to/a/file << EOF
	-   I am $USER
	-   EOF

>一般使用输入输出重定向到系统文件，需要备个份哈。
- wc -l < /etc/passwd

- read var < a.txt
- echo $var
- \> 原有内容会清空
- \>> 追加
- 2> 错误重定向
- &> 全部重定向

### 拆分大文件genome到小文件
序列操作

1. 反义互补

$ echo 'ATTGCTATGCTNNNT' | rev | tr 'ACTG' 'TGAC'
ANNNAGCATAGCAAT

2. 将fasta文件分割成多个文件，一个文件一个fasta序列

	csplit -z -q -n 4 -f sequence_ test.fa /\>/ {*}

3.	同时你也可以用awk来使用
	awk '/^>/{s="NC_029256"++d".1.fa"} {print > s}' test.fa
	awk '/^>/{s=++d".fa"} {print > s}' test.fa

> [只用一行来颠覆你处理文件的方式](https://cloud.tencent.com/developer/article/1613814)

1. 脚本编程
## C语言学习笔记
    // In general, the two expressions drinks[i] and *(drinks + i)
    // are equivalent

```c
int drinks[] = {4, 2, 3};
printf("1st order: %i drinks\n", drinks[0]);
printf("1st order: %i drinks\n", *drinks)
```
### Pointer
Array variables can be used as 
pointers…



