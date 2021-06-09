
# -*- coding: utf-8 -*-
# 使用K-means对图像进行聚类，显示分割标识的可视化
import PIL.Image as image
import numpy as np
from sklearn.cluster import  KMeans
from sklearn import preprocessing
from skimage import color
#  加载图像，并对数据进行规范化

def load_data(filePath):
    # 读文件
    f = open(filePath,'rb')
    data = []
    # 得到图像的像素值
    img = image.open(f)
    # print(img)
    # 得到图像尺寸
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # 得到点(x, y)的三个通道值
            c1, c2, c3 = img.getpixel((x, y))
            # print(img.getpixel((x, y)))
            data.append([c1, c2, c3])
    f.close()
    # 采用Min-Max规范化
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data)
    return np.mat(data), width, height

# 加载图像，得到规范化的结果img, 以及图像尺寸
img, width, height = load_data("../data/weixin.jpg")

# 用K-Means对图像进行2聚类
kmeans = KMeans(n_clusters=16)
kmeans.fit(img)
label = kmeans.predict(img)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape(width, height)
# 创建个新图像pic_mark，用来保存图像聚类的结果，并设置不同的灰度值
pic_mark = image.new("L", (width, height))

# 创建个新图像img，用来保存图像聚类压缩后的结果
img = image.new("RGB", (width, height))
for x in range(width):
    for y in range(height):
        # 根据类别设置图像灰度，类别0灰度值为255，类别1灰度值127
        pic_mark.putpixel((x, y), int(256/(label[x][y]+1))-1)

        c1 = kmeans.cluster_centers_[label[x, y], 0]
        c2 = kmeans.cluster_centers_[label[x, y], 1]
        c3 = kmeans.cluster_centers_[label[x, y], 2]
        img.putpixel((x, y), (int(c1*256) - 1, int(c2*256) - 1, int(c3*256) -1))
pic_mark.save("weixin_mark.jpg","JPEG")

img.save('weixin_new.jpg')
# 将聚类标识矩阵转化为不同颜色的矩阵
label_color = (color.label2rgb(label)*255).astype(np.uint8)
label_color = label_color.transpose(1, 0, 2)
images = image.fromarray(label_color)
images.save('weixin_mark_color.jpg')


