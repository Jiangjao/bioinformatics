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

## 添加数据 & fire
<!-- I’m inserting 400,000 rows with the ORM and it’s really slow! -->
```python
import contextlib
import sqlite3
import sys
import tempfile
import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import __version__, Column, Integer, String, create_engine, insert
from sqlalchemy.orm import Session
mport contextlib
import sqlite3
import sys
import tempfile
import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import __version__, Column, Integer, String, create_engine, insert
from sqlalchemy.orm import Session
@contextlib.contextmanager
def sqlalchemy_session(future):
    with tempfile.NamedTemporaryFile(suffix=".db") as handle:
        dbpath = handle.name
        engine = create_engine(f"sqlite:///{dbpath}", future=future, echo=False)
        session = Session(
            bind=engine, future=future, autoflush=False, expire_on_commit=False
        )
        Base.metadata.create_all(engine)
        yield session
        session.close()

def test_sqlalchemy_core(n=100000, future=True):
    with sqlalchemy_session(future) as session:
        with session.bind.begin() as conn:
            t0 = time.time()
            conn.execute(
                insert(Customer.__table__),
                [{"name": "NAME " + str(i)} for i in range(n)],
            )
            conn.commit()
            print("SQLA Core", n, time.time() - t0)
```
## 引用
>[ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)

>[sqlalchemy](https://www.osgeo.cn/sqlalchemy/index.html)

>[Python通过ORM方式操作MySQL数据库](https://blog.csdn.net/HG0724/article/details/112332393)

>[Python连接数据库 ORM——插入，查询， 修改，删除](https://blog.csdn.net/weixin_46549605/article/details/123170145)

>[Speed up the performance of sqlalchemy](https://docs.sqlalchemy.org/en/14/faq/performance.html)