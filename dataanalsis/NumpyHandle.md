# 04 | Python 科学计算：用Numpy快速处理数据

    由于Python 编程隐去了指针的概念，但是数组是有指针的，Python的列表list就是数组。
    如:[0,1,2]，就需要三个指针和三个整数的对象
    这样对于Python来说是非常不经济的，浪费了内存和时间

## 使用Numpy让你的Python科学计算更高效
    list元素在系统内存中是分散的，而Numpy数组存储在一个均匀连续的内存块中。
    这样数组遍历所有的元素怒，不像列表list还需要对内存地址进行查找，
    从而节省了计算资源

    另外在内存访问模式中，缓存会直接把字节块从 RAM 加载到 CPU 寄存器中。因为数据连续的存储在内存中，NumPy 直接利用现代 CPU 的矢量化指令计算，加载寄存器中的多个连续浮点数。另外 NumPy 中的矩阵计算可以采用多线程的方式，充分利用多核 CPU 计算资源，大大提升了计算效率。

    当然除了使用 NumPy 外，你还需要一些技巧来提升内存和提高计算资源的利用率。
一个重要的规则就是：**避免采用隐式拷贝，而是采用就地操作的方式**。
    举个例子，如果我想让一个数值 x 是原来的两倍，可以直接写成 x*=2，而不要写成 y=x*2

    在 NumPy 里有两个重要的对象：
-   ndarray（N-dimensional array object）解决了多维数组问题，
-   ufunc（universal function object）则是解决对数组进行处理的函数。

## ndarray 对象
    ndarray 实际上是多维数组的含义。在 NumPy 数组中，维数称为秩（rank），一维数组的秩为 1，二维数组的秩为 2，以此类推。在 NumPy 中，每一个线性的数组称为一个轴（axes），其实秩就是描述轴的数量。
### 创建数组
```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1,1]=10
print(a.shape) 
print(b.shape) 
print(a.dtype) 
print(b) 
```

### 结构数组
    实际上在 C 语言里，可以定义结构数组，也就是通过 struct 定义结构类型，结构中的字段占据连续的内存空间，每个结构体占用的内存大小都相同

```python

import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei",32,75,100, 90),("GuanYu",24,85,96,88.5),
       ("ZhaoYun",28,85,92,96.5),("HuangZhong",29,65,85,100)],
    dtype=persontype)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print np.mean(ages)
print np.mean(chineses)
print np.mean(maths)
print np.mean(englishs)
```
## ufunc 运算
    universal function
    NumPy 中很多 ufunc 函数计算速度非常快，因为都是采用 C 语言实现的。

### 连续数组的创建
    linspace 是 linear space 的缩写，代表线性等分向量
```python

x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print np.add(x1, x2)
print np.subtract(x1, x2)
print np.multiply(x1, x2)
print np.divide(x1, x2)
print np.power(x1, x2)
print np.remainder(x1, x2) # which is equal to np.mod(x1, x2)
```

## 统计函数
    略，建议
    查查官方文档

## NumPy 排序
    排序是算法中使用频率最高的一种，也是在数据分析工作中常用的方法，计算机专业的同学会在大学期间的算法课中学习。

    那么这些排序算法在 NumPy 中实现起来其实非常简单，一条语句就可以搞定。这里你可以使用 sort 函数，sort(a, axis=-1, kind=‘quicksort’, order=None)，默认情况下使用的是快速排序；在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序。同样 axis 默认是 -1，即沿着数组的最后一个轴进行排序，也可以取不同的 axis 轴，或者 axis=None 代表采用扁平化的方式作为一个向量进行排序。另外 order 字段，对于结构化的数组可以指定按照某个字段进行排序。

```python
a = np.array([[4,3,2],[2,4,1]])
print np.sort(a)
print np.sort(a, axis=None)
print np.sort(a, axis=0)  
print np.sort(a, axis=1)  
```

写写作业啥的...


