import PIL.image as image
#  加载图像，并对数据进行规范化

def load_data(filePath):
    # 读文件
    f = open(filePath,'rbb')
    # 得到图像的像素值
    img = image.open(f)
    # 得到图像尺寸
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # 得到点(x, y)的三个通道值
            c1, c2, c3 = img.getpixel(x, y)









