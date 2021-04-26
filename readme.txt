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
