# !/usr/bin/python3
# <!--encoding='utf-8'-->

import matplotlib.pyplot as plt
import pylab
# pip install opencv-python
import cv2
import numpy as np
from scipy import signal
# 设置原图像
# img = np.array([[10,10,10,10,10],
#                 [10,5,5,5,10],
#                 [10,5,5,5,10],
#                 [10,5,5,5,10],
#                 [10,10,10,10,10]]
#                 )

# 设置卷积核
# fil = np.array([[-1,-1,0], 
#                 [-1, 0, 1], 
#                 [ 0, 1, 1]])
# 对图像进行卷积操作
# res = signal.convolve2d(img, fil, mode='valid')
# 输出卷积后的结果
# print(res)

# 读取灰度图像
img = cv2.imread("weixin_new.jpg",0)

# 显示灰度图像
plt.imshow(img,cmap="gray")
pylab.show()

# 设置卷积核
fil = np.array([[ -1, -1, 0],
                [ -1,  0, 1], 
                [  0,  1, 1]])
# 卷积操作
res = signal.convolve2d(img, fil, mode='valid')
print(res)
# 显示卷积后的图片
plt.imshow(res, cmap="gray")
pylab.show()
    

