import re
import csv
from io import StringIO
strings = """sampleName\tcancer\toutcome\tbatch\tsample\tF
GSM71019_CEL\tNormal\tNormal\t3a\t1a\t
GSM71020_CEL\tNormal\tNormal\t2a\t2a\t1\t
"""

contains_digit = False

def is_number(string):
    return re.search(r'^\d+$', string)

def is_empty(string):
    return len(row[i]) == 0

data = StringIO(strings)
temp = csv.reader(data, delimiter="\t")

rows = []
for line in temp:
    # reader = csv.DictReader(line)
    column = [row for row in line]
    rows.append(column)
    # print(column)

# print(rows)

column_header = rows[0]
has_number = [False] * len(column_header)

for i in range(len(column_header)):
    for row in rows:
        if is_number(row[i]):
            has_number[i] = True
            # break

strjoin = ""
for i, v in enumerate(has_number):
    if v:
        print(i)
        # column_header.pop(i)
        strjoin += column_header[i] + " "

# print(has_number)
print(column_header)
print(strjoin)
# with open('data.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         rows.append(row)

# print(temp)
# reader = csv.DictReader(data, delimiter='\t')
# for rows in reader:
#     print(rows)
# rows = list(reader)
# print(rows)

for line in strings.split('\n'):
    if line:
        for item in line.split("\t"):
            if is_number(item):
                contains_digit = True
                break

if contains_digit:
    print("Contains digit")
else:
    print("Not contains digit")