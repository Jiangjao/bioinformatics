# !/usr/bin/python3
# -- encoding = utf-8 ---
# editor:xiaojiao 2022/10/18

# Process pool & Process map 
# preparation for loading data to database...
# source from
# https://blog.csdn.net/weixin_38819889/article/details/107815272


# [python tutor]: process 、map progress bar : https://zhuanlan.zhihu.com/p/359369130
from ast import Assert
import time
from multiprocessing import Pool, Process
import random, os

# TODO(xiaojiao): traverse folder

def travelDir(path, all_file = None):
    if all_file == None:
        all_file = []
    if os.path.exists(path):
        files = os.listdir(path)
    else:
        print("This path not exist")
        # AssertionError "this"
        assert 'This path not exist'
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            travelDir(os.path.join(path, file), all_file)
        else:
            all_file.append(os.path.join(path, file))
    return all_file

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

def func3(folder_list:list):
    for file in folder_list:
        yield file

def test2(folder_list:list):
    """
        Process pool
    """
    pool = Pool(processes=5)

    for i in folder_list:
        pool.apply_async(func=fun2, args=(i, ))

    pool.close()
    pool.join()

    print("end of test")

if __name__ == "__main__":
    # test1()
    folder_list = [".", 2, 3]
    test2(folder_list)
    # subprocess.run(['dir'])
    # pass
    # currentFloder = travelDir(".")
    # print(currentFloder)

    # temp = func3(folder_list)










