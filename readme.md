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
## 66 | 转义和引用
### 特殊字符
	字面意义，元意(meta-meaning)
-	#注释
-	;分号
-	\转义符号
-	"和'引号
### 转义符号
	单个字符前的转义符号
-	\n \r\t 单个字母的转义
-	\$ \" \\ 单个非字母的转义

## 66 | 运算符
-	赋值运算符
	- \+ - * // ** %
	- 使用`expr`进行运算
	- **数字常量**的运算
-	算数运算符
	- 
-	数字常量
-	双圆括号
	- 是let命令的简化

## 89 | sed替换命令讲解
- sed 的基本工作方式
  - 将文件以行为单位读取到内存（模式空间）
  - 使用sed的每个脚本对改行进行操作
  - 处理完成后输出该行

## 94 | AWK和sed的区别
-    AWK更像脚本语言
-    AWK用于"比较规范"的文本处理，用于统计数量并输出指定字段
-    使用sed将不规范的文本，处理为"比较规范"的文本
-    AWK脚本的流程控制
    -  输入数据前例程BEGUN{}
    - 主输入循环{}
    - 所有文件读取完成例程END{}

## 96 | AWK表达式
-   赋值操作符
-   算数操作符
-   系统变量
-   关系操作符
-   布尔操作符

### awk中的'系统变量'
-   FS和OFS字段分隔符，OFS表示输出的字段分隔符
-   RS记录分隔符
-   NR和FNR行数
-   NF字段数量，最后一个字段可以用$NF取出

## awk 判断和循环
-   条件语句使用if开头,根据表达式的结果来判断执行哪条语句
-   如果有多个语句需要执行可以使用{}将多个语句括起来

### 98 | awk数组
-   数组的定义
-   数组的遍历
-   删除数组
-   命令行参数数组
### 拆分大文件genome到小文件
序列操作

## linux系统自带函数库介绍
/etc/init.d/functions
/etc/profile 系统文件变量
~/.bashrc bashrc 执行顺序
.bash_profile

平时使用时，source命令导入就行。
1. 反义互补

$ echo 'ATTGCTATGCTNNNT' | rev | tr 'ACTG' 'TGAC'
ANNNAGCATAGCAAT

2. 将fasta文件分割成多个文件，一个文件一个fasta序列

	csplit -z -q -n 4 -f sequence_ test.fa /\>/ {*}

3.	同时你也可以用awk来使用
	awk '/^>/{s="NC_029256"++d".1.fa"} {print > s}' test.fa
	awk '/^>/{s=++d".fa"} {print > s}' test.fa

> [只用一行来颠覆你处理文件的方式](https://cloud.tencent.com/developer/article/1613814)

### cut 命令详解释
    cut命令的选项

Cut基本语法：

cut OPTION... [FILE]...

选项：

`-f` : 通过指定哪一个字段进行提取。cut命令使用***`TAB`***作为默认的字段分隔符。
`-d` : “TAB”是默认的分隔符，使用此选项可以更改为其他的分隔符。
`--complement` : 此选项用于排除所指定的字段。
--output-delimiter : 更改输出内容的分隔符。
----
有点儿意思
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



