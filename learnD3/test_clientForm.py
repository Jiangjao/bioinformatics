import json
import csv
from random import uniform
from types import FunctionType
from io import StringIO
import re

group_choices = []



def is_number(string):
  return re.search(r'^\d+$', string)

def is_empty(string):
    return len(string) == 0

def set_groups_names(
    ClientForm: dict,
    Trigger: str,
    PrevValue: dict,
    fileContent: FunctionType,
    cacheGet: FunctionType
):
    default_help = (
        "制表符文件"
    )

    arg_default = dict(
        type="map_group",
        name="分组方案名",
        multiple=True, 
        safe=True,
        choices=group_choices
        )
    return arg_default


def get_gene_arg(
    ClientForm: dict,
    Trigger: str,
    PrevValue: dict,
    fileContent: FunctionType,
    cacheGet: FunctionType  
):

    default_help = (
        "制表符文件"
    )

    arg_default = dict(
        type="map",
        name="分组信息表",
        help=f"{default_help}"
    )
    # return arg_default

    # print("Trigger>>>", Trigger)
    mapping_file = ClientForm["mapping_file"]
    print("ClientForm mapping_file >>>", mapping_file)
    # TODO:xiaojiao, 获取mapping_file后, 需要遍历mapping_file, 
    # 2. 查询到mapping_file 哪一列有数字，
    # 3. 标记该列
    # print("filecontent>>>", fileContent)

    if not mapping_file: 
        return arg_default

    contains_digit = False

    for line in mapping_file.split('\n'):
        if line:
            for item in line.split("\t"):
                if is_number(item):
                    contains_digit = True
                break
    print("contains_digit >>", contains_digit)

    contains_digit = False

    data = StringIO(mapping_file)
    temp = csv.reader(data, delimiter="\t")

    rows = []
    for line in temp:
        column = [row for row in line]
        rows.append(column)
    print(column)

    print(rows)

    column_header = rows[0]
    has_number = [False] * len(column_header)
    strjoin = ""

    for i in range(len(column_header)):
        for row in rows:
            if is_number(row[i]):
                has_number[i] = True
                # break

    for i, v in enumerate(has_number):
        if v:
            print(i)
            strjoin += column_header[i] + " "
            column_header.pop(i)

    if not is_empty(strjoin):
        arg_default["help"] = (
            f"{default_help}"
            '<span style="color: red">'
            f" 该 {', '.join(strjoin)}列包含数字, 不将作为分组方案名"
            '</span>'
            f";"
        )

    group_choices = column_header
    # ClientForm["group_choices"] = column_header
    print(has_number)
    print(column_header)


    # TODO:Xiaojiao, 获取输入文件的列，在这边显示
    return arg_default

