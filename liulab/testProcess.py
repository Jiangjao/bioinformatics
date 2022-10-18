# !/usr/bin/python3
# -- encoding = utf-8 ---
# editor:xiaojiao 2022/10/18

# Process pool & Process map 
# preparation for loading data to database...
# source from
# https://blog.csdn.net/weixin_38819889/article/details/107815272


# [python tutor]: process 、map progress bar : https://zhuanlan.zhihu.com/p/359369130
import time
from multiprocessing import Pool, Process
import random, os

def numsCheng(i):
    return i * 2


# 最重要的一点，多进程必须在 if __name__ == '__main__' 下写！
# 否则会报错，当然了，你在函数里使用多进程，
# 然后在 if __name__ == '__main__' 下调用这个函数也是允许的。
def test1():
    """
        Suitable for CPU computing tasks
    """
    time1 = time.time()
    # nums_list has to be iterable
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pool = Pool(processes=5)
    result = pool.map(numsCheng, nums_list)
    pool.close()
    pool.join()

    print(result)
    time2 = time.time()
    print("计算用时:", time2 - time1)

def fun2(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))

def test2():
    """
        Process pool
    """
    pool = Pool(processes=5)

    for i in range(15):
        pool.apply_async(func=fun2, args=(i, ))

    pool.close()
    pool.join()
    
    print("end of test")

if __name__ == "__main__":
    # test1()
    test2()










