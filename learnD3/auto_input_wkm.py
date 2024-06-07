# !/usr/bin/python3
# xiaojiao

# https://learn.microsoft.com/zh-cn/microsoft-edge/webdriver-chromium/?tabs=c-sharp
# https://link.csdn.net/?target=https%3A%2F%2Fgooglechromelabs.github.io%2Fchrome-for-testing%2F
# https://chromedriver.storage.googleapis.com/index.html
# https://googlechromelabs.github.io/chrome-for-testing/#stable
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import random
from selenium import webdriver
import pandas
from scipy.spatial import distance

# 确实，直接放到当前项目路径下即可
# 配置chromedriver.exe 在当前目录下即可
# chromedriver_path = r"C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chromedriver_path)

url = "http://bioincloud.tech:8788/#/standalone-task-ui/dynamic_grid_heatmap_with_mantel_test"
import numpy as np

matrix = np.array([ [1, 0.8210576858123295, 0.8705892711689287, 0.824566479341442, 0.8541313718020874, 0.7398956945034544, 0.4780323726958185, 0.8280752728705546, 0.9193039046274801, 0.7929873375794294, 0.7684257828756417, 0.8014072130488722, 0.8386016534578921], 
                    [0.0, 1.0, 0.9329146104170898, 0.8811188811188813, 0.833626497322632, 0.8126107032724816, 0.6409817185295869, 0.7762237762237763, 0.8951048951048951, 0.8811188811188813, 0.8741258741258742, 0.8056054385890983, 0.8181818181818183], [0.0, 0.0, 1.0, 0.830435353969758, 0.812421193401995, 0.7982613468938993, 0.4708148963941845, 0.6926184228854153, 0.9117120056348833, 0.8056989817238502, 0.7668275396231382, 0.757551788183124, 0.8198340515786545], [0.0, 0.0, 0.0, 1.0, 0.9106844088398501, 0.9422080999150758, 0.7075317330217298, 0.8181818181818183, 0.8741258741258742, 0.9510489510489512, 0.8951048951048951, 0.7145369977051133, 0.7342657342657343], [0.0, 0.0, 0.0, 0.0, 1.0, 0.8596491228070177, 0.775438596491228, 0.6795106742881959, 0.9281975705483089, 0.8511396590310907, 0.9071817764981586, 0.636842105263158, 0.7075317330217298], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.5982456140350878, 0.6514896155546621, 0.8266212326392487, 0.8931712471313915, 0.7635738504887974, 0.5508771929824562, 0.6409817185295869], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.4903685278368424, 0.612960659796053, 0.5919448657459025, 0.8021028062474065, 0.3087719298245614, 0.3047290137271806], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.6923076923076924, 0.8391608391608393, 0.7552447552447553, 0.8616475560561659, 0.7762237762237763], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.8181818181818183, 0.8601398601398602, 0.7390554240969553, 0.8041958041958043], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.8461538461538463, 0.8021028062474066, 0.8321678321678322], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.7250448947301884, 0.6643356643356644], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.9422080999150758], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
                   
transposed_matrix = matrix.T

print(transposed_matrix)

def has_duplicate(nums):
    """判断列表是否有重复元素

    Args:
        names (list): names

    Raises:
        ValueError: info

    Returns:
        boolean: _description_
    """
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    
    return xor_sum != 0
# 登录百度
def main(url):
    driver.get(url)


# pandas.
# driver.implicitly_wait(3 * random.random() ) #设置等待3秒后打开目标网页

# driver = webdriver.Chrome()

# https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/first_script/
# 发送文件
# driver.get('http://bioincloud.tech:8788/#/standalone-task-ui/dynamic_grid_heatmap_with_mantel_test')
# title = driver.title
# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()

# time.sleep(5)
# driver.quit()


if __name__ == '__main__':
    # main(url)
    pass