from collections import Counter
import pandas as pd
from collections import defaultdict
import math
import csv
counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int))) 

def is_number(s):
    """判断字符串由数字组组成, 并且不是NaN

    Args:
        s (_type_): string

    Returns:
        _type_: bool
        
    # 测试字符串和数字
    print(is_number('foo'))   
    # False
    print(is_number('1'))    
    # True
    print(is_number('1.3'))  
    # True
    print(is_number('-1.37')) 
    # True
    print(is_number('1e3'))  
    # True
    print(is_number(math.nan))  
    # False
    """
    if s == None:
        return False
    
    # TODO:xiaojiao, 是否加上math.isfinite
    try:
        if isinstance(s, str):
            num = float(s.strip())
            # 去除NaN
            if math.isnan(num):
                return False
            return True
        # 如果是数字
        float(s)
        return True
    except ValueError:
        pass
 
    return False
# 读取文件
# df = pd.read_csv('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count_particle.tsv',
#                  sep='\t',
#                  header=0)

df = pd.read_csv('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count.tsv',
                 sep='\t',
                 header=0)
nested_list = []

column_names = []

index = 0

# summary
# 读取文件 
with open('C:/Users/Cherry/Desktop/geekbang/bioinformatics/learnD3/detailed_gene_count_particle_duplicate.tsv') as f:
    lines = f.readlines()
    # lines = f.readlines()
    headers = lines[0].split('\t')

    # column_names.append(headers)
    for line in lines[1:]:
        values = line.split('\t')
        gene = values[0]
        for i, value in enumerate(values[1:]):
            sample = headers[i + 1]
            
            if is_number(value):
                if sample not in column_names:
                    # 获取列名
                    column_names.append(sample)
        index = index + 1
        if index >= 3:
            column_names.insert(0, headers[0])
            break
                # counts[gene][sample] = float(value)

    # column_names.append(headers)
    for line in lines[1:]:
        values = line.split('\t')
        gene = values[0]
        for i, value in enumerate(values[1:]):
            sample = headers[i + 1]
            if is_number(value):
                # counts[gene][sample] = counts[gene].get(sample, 0) + float(value)
                counts.setdefault(gene, {})[sample] =  counts[gene].get(sample, 0) + float(value)

# abundance_data = []

index = 0
for gene, samples in counts.items():
    row = [gene]
    for sample, count in samples.items():

        row.append(count)
    nested_list.append(row)


print(nested_list)
nested_list = [column_names] + nested_list
# 提取基因名称 
# genes = [line.split('\t')[0] for line in lines[1:]]

# # 使用字典计数
# counts = {}
# for gene in genes:
#     counts[gene] = counts.get(gene, 0) + 1


print(counts)
# 使用Counter统计每个基因名称的计数
# counts = Counter(genes)

# 输出统计结果
print(counts)