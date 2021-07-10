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

## 48 | i节点和数据块操作
-   Hard link (ln sourceFile destFile)

通常要求文件和链接位于同一文件系统中
Hard link与源文件几乎没有区别, 只能通过ls -li看出link关系
删除源文件后, Hard link文件仍然存在,保留了源文件的内容

-   Symbol link (ln -s sourceFile linkFile)

可以指向文件夹和不在同一磁盘的文件
删除源文件后, Symbol link仍然存在, 但是内容不存在

-   链接数目 (hard link)

对于文件而言, 代表链接的数量;
对于目录而言, 指的是命名的目录项, 目录项中的 . 以及子目录中的 ..

## 54 | 系统综合状态查看命令sar以及第三方命令
Linux Performance
>http://www.brendangregg.com/linuxperf.html

Install and Configure SAR

For Debian/Ubuntu
```bash
# sudo apt-get install sysstat
```

For RedHat/CentOS
```bash
sudo yum install sysstat
```
#sudo vi /etc/default/sysstat 
ENABLED="true"
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

## 90 | sed的替换指令加强版

### 标志位
-   数字，第几次出现才进行替换
-   g, 每次出现都进行替换
-   p 打印模式空间的内容
    -   sed -n 'script' filename 阻止默认输出
-   w file 将模式空间的内容写入到文件

### 寻址
默认对每行进行操作,增加寻址后对匹配的行进行操作
-   /正则表达式/s/old/new/g
-   行号s/old/new/g
    -   行号可以是具体的行，也可以是最后一行$
-   可以使用两个寻址符号，也可以混合使用行号和正则表达式
### 分组
-   寻址可以匹配多条命令
-   /regular/ { s/old/new/;s/old/new/ }

### 脚本文件
-   可以将选项保存为文件，使用-f加载脚本文件
-   sed -f sedscript filename

>https://www.gnu.org/software/sed/manual/sed.html 英文文档
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

## 非root 用户安装软件注意哈，指定prefix 
```bash
tar -zvxf cmake-3.14.5.tar.gz
$ cd cmake-3.14.5
$ ./bootstrap
$ ./configure --prefix=/home/xxx/cmake            !!!注意，要在自己用户名下的目录配置，如果不加--prefix会默认在root目录下配置，这样后面make install时没有sudo权限会失败
$ make
$ make install
```

### LINUX 暂停、继续进程
kill -STOP 1234 将该进程暂停。

如果要让它恢复到后台，用kill -CONT 1234 （很多在前台运行的程序这样是不行的）

如果要恢复到前台，请在当时运行该进程的那个终端用jobs命令查询暂停的进程。

然后用 fg 〔job号〕把进程恢复到前台

1. command& 让进程在后台运行

2. jobs 查看后台运行的进程

3. fg %n 让后台运行的进程n到前台来

4. bg %n 让进程n到后台去；  

   PS:"n"为jobs查看到的进程编号
5. 以下命令在后台执行 root 目录下的 runoob.sh 脚本：
   nohup /root/runoob.sh &
### 指定进程在cpu上

查看进程
```bash
-> % ps
  PID TTY          TIME CMD
 2683 pts/1    00:00:00 zsh
 2726 pts/1    00:00:00 dgram_servr
 2930 pts/1    00:00:00 ps
```
查看cpu的位置
```bash
-> % taskset -p 2726
pid 2726's current affinity mask: 3
```

选定cpu
```bash
-> % taskset -pc 1 2726
pid 2726's current affinity list: 0,1
pid 2726's new affinity list: 1
```


### git 更新ignore 文件
```bash
git rm -r --cached . // 删除本地缓存
git add . // 添加要提交的文件
git commit -m 'update .gitignore' // 更新本地的缓存
```



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

### 不同整型的输出
使用不同的格式控制符可以输出不同类型的整数，它们分别是：
`%hd`用来输出 short int 类型，hd 是 short decimal 的简写；
`%d`用来输出 int 类型，d 是 decimal 的简写；
`%ld`用来输出 long int 类型，ld 是 long decimal 的简写。

### 字符串的两种形式

```c
char str1[] = "http://c.biancheng.net";
char *str2 = "c语言编程网";

```
一种形式的字符串所在的内存既有读取权限又有写入权限，第二种形式的字符串所在的内存只有读取权限，没有写入权限。printf()、puts() 等字符串输出函数只要求字符串有读取权限，而 scanf()、gets() 等字符串输入函数要求字符串有写入权限，所以，第一种形式的字符串既可以用于输出函数又可以用于输入函数，而第二种形式的字符串只能用于输出函数。
权限不一样，从sysstdin读取的权限高且多些。

### make的多种作用
make可以做得更多，但是我们没有空间在这里讨论。关于
make的更多信息和功能，请浏览 GNU Make Manual：
 http://tinyurl.com/yczmjx
 
### 清空缓冲区
// 将换行符前面的所有字符清空，scanf("%*c");将最后的换行符清空
scanf("%*[^\n]");scanf("%*c");

scanf("%*[^\n]%*c");
这是错误的。合并以后的语句不能清空单个换行符，因为该语句要求换行符前边至少要有一个其它的字符，单个换行符会导致匹配失败。

scanf()
控制字符串的完整写法为：
%{*}{width}type

### 运算符优先级
逻辑运算符和其它运算符优先级从低到高依次为：
赋值运算符(=) < &&和|| < 关系运算符
< 算术运算符
< 非(!)

### 数组的初始化
1) 赋值是有次序的，可以给部分元素赋初值，当（）中的值少于元素个数时，只给前面的元素赋值；当赋值的元素少于数组总体元素时，剩余的元素自动赋值？
   
### 二维数组
二维数组在概念上是二维的，但在内存中地址是连续的，也就是说存储器单元是按照一维线性排列的。
-   按行排列，一行又一行
-   按列排列，一列又一列

### 获取字符串
如果希望读取的字符串中不包含空格，那么使用scanf()函数；如果希望获取整行字符串，那么使用gets函数，它可以避免空格的截断。

### 预处理功能
是C语言特有的功能，它是对源程序正式编译前预处理程序完成的，
实际上是对资源的distribution
宏喜欢先进行符号替换

### 指针
数据和代码都以二进制的形式存储在内存中，计算机无法凑够格式上区分某块内存存储的是数据还是代码。当程序杯加载到内存中，操作系统会给不同的内存块指定不同的权限，拥有读取和执行的权限的内存块就是代码，而拥有读取和写入权限的内存块就是数据。

CPU只能通过地址来取得内存中的代码和数据，如果任意访问，就会出错。
无论指针还是取地址符(&)，解引用(*)啥的，理清楚源头，探明其精微，大概就清楚怎么用了。
>https://blog.csdn.net/synapse7/article/details/10260339
