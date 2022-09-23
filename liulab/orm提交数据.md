# ORM是？:cherry_blossom:
&emsp;&emsp;[`ORM`](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping),Object–relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between type systems using object-oriented programming languages
其实就是将sql语言包装成对象，实现对象的CURD操作
&emsp;&emsp;在wiki上，可以看一下它的overview。大致有一个了解

## ORM 创建表
```python
from sqlalchemy import create_engine
# 注意这里使用的是sqlite
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# 业务逻辑
# 持久层
# 数据库层

# 实例一个引擎, lazy initialization
dburl = 'mysql+pymysql://root:password@localhost:3306/table?charset=utf8mb4'
engine = create_engine(dburl, echo=True,encoding='utf-8')
```

## 获取数据
```python
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

############### ###############
# 实际上它相当于:
# BEGIN (implicit)
# select 'hello world'
# [...] ()
# [('hello world',)]
# ROLLBACK
############### ###############
```

## 创建表
&emsp;&emsp;[`官方介绍`](https://www.osgeo.cn/sqlalchemy/tutorial/metadata.html)

首先获取database,然后创建table.
```python
from sqlalchemy import MetaData
metadata_obj = MetaData()

from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

# 向数据库发送DDL
metadata_obj.create_all(engine)
```

## 引用
>[ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)

>[sqlalchemy](https://www.osgeo.cn/sqlalchemy/index.html)

>[Python通过ORM方式操作MySQL数据库](https://blog.csdn.net/HG0724/article/details/112332393)