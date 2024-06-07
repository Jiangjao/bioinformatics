#Geneid ....
Xkr4 ...
Xkr4, Xkr4...

```python
# dict["Geneid"] =""
# dict["Geneid"] ="Xkr4"
# dict["Geneid"] ="Xkr4 Xkr4,Xkr4"
# 1.数据结构 ，这种特殊字符串的行成过程
random_string = hashlib.md5(os.urandom(32)).hexdigest()
value_pre = dict.get("Geneid", "")

for substring in value_pre.split(random_string):
    # newstring 是新传入的字符串
    if newstring not in substring:
        dict["Geneid"] = f"{value_pre}{random_string}{newstring}"
    else:
        if len(substring.strip()) == len(newstring.strip()):
            # 基本上判定一致
            dict["Geneid"] = f"{value_pre}"

```

2. 在运行时
需要判定“Xkr4”是否在dict["Geneid"]中是否存在