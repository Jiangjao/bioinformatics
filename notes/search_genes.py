# /usr/bin/python3
# -- encoding: utf-8 -

import requests
import functools
from bs4 import BeautifulSoup
import bs4

# 发送HTTP请求
url = "http://www.autophagy.lu/clustering/index.html"
response = requests.get(url)

# 解析HTML页面
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# 从第四个table开始
global flag
flag = True

def extract_table_data(table):
    """
    提取单个表格的数据

    table like this:


    <table width="100%">
        <tr>
            <td width="30%">
                <a href="http://www.lih.lu" style="border-color:white">
                    <img alt="LIH" height="" src="/Supplements/Pictures/public-research-center.png" style="border-color:white" title="LIH" width=""/>
                </a>
            </td>
            <td width="40%"></td>
            <td id="update_in_progress" style="border-color:red;text-align:right;font-size:12px" width="30%">
                <!--- marquee -->
                Update in progress
                <!---/marquee-->
            </td>
        </tr>
    </table>
    """


    soup = BeautifulSoup(str(table), 'html.parser')
    table = soup.table
    rows = table.find_all('tr')

    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        print(row_data)
        load_into_file(row_data)

def load_into_file(line):
    # 去重不必要的字符
    line = [element.replace("\n", "").replace("\t","") for element in line]
    # line =  ','.join(str(line).split())
    
    # 由于tables是GeneId	Name	Symbol的结构（三个字符)
    # 起始字符GeneId是数字
    # 只需要判断line长度起码在3
    length = len(line)
    if length >=3:
        line_start = line[0]
        # 起始字符GeneId不是数字，舍弃
        if not line_start[:1].isdigit():
            return
        with open("./gene_temp.csv", mode="a+", encoding="utf-8") as f:
            f.write(",".join(line))
            f.write("\n")
        print("**** genes list ****")
        print(line[-1], file=open("./gene_temp.txt", mode="a+", encoding="utf-8"))
    # for element in line:
    #     print(element.strip(), file=open("./gene_temp.txt", mode="a+", encoding="utf-8"))
    #     print("\n")
# functools模块中的lru_cache装饰器来优化函数的性能。
# lru_cache装饰器会缓存函数的结果，并且在后续调用相同参数的函数时，直接返回缓存的结果，避免重复计算
@functools.lru_cache(maxsize=None)
def extract_all_tables(soup):
    """
    递归地提取所有表格的数据
    """
    all_data = []
    # if all_data == []:
    #     tables = soup.find_all('table')[:4]
    #     flag = False
    # else:
    tables = soup.find_all('table')
    valid_tables = []  # 保存有效的HTML标签对象
    for table in tables:
        if isinstance(table, bs4.element.Tag):  # 判断是否为HTML标签对象
            valid_tables.append(table)
    if valid_tables:
        # 第四个table
        for table in tables:
            # data = extract_table_data(table)
            # all_data.append(data)
            if len(table.find_all('table')) > 0:
                sub_soup = BeautifulSoup(str(table), 'html.parser')
                sub_data = extract_all_tables(sub_soup)
                # all_data += sub_data
            else:
                yield table
    # return all_data

# 解析HTML代码
# soup = BeautifulSoup(html, 'html.parser')

# 提取所有表格的数据
# tables = soup.find_all('table')[:3]
# tables = BeautifulSoup(str(tables), 'html.parser')
soup = BeautifulSoup(response.content, 'html.parser')
all_data = extract_all_tables(soup)

# print(all_data)
for table in all_data:
    # print(table)
    extract_table_data(table)

# 打印结果
# for data in all_data:
#     for row in data:
#         # print('\t'.join(row))
#         print(','.join(row), file=open("./gene_temp.txt", mode="w+", encoding="utf-8"))
#     print('-' * 20)
    
# # 找到表格并提取数据
# tables = soup.find_all('table')[4]
# # 打印所有表格的数据
# for table in soup.find_all('table')[4]:
#     rows = table.find_all('tr')
#     data = []
#     for row in rows:
#         cols = row.find_all('td')
#         cols = [col.text.strip() for col in cols]
#         data.append(cols)

#     # 打印表格数据
#     for row in data:
#         print(','.join(row), file=open("./gene_temp.txt", mode="w+", encoding="utf-8"))
#     print('-' * 20)

