# !/usr/python3
# encoding = utf-8

import traceback
import time
from mysql import connector
from dbconfig import read_db_config
# from purfied_data import purfied_data
# from config import my_sql_config
# 打开数据库连接
dbserver = read_db_config()
# dbserver = read_db_config()
# db = connector.connect(**dbserver)



# 0.连接上数据库

db = connector.connect(pool_name = "mypool",
										pool_size = 3,
										**dbserver)

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# cursor = db.cursor(buffered=True)
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("MySQL版本:%s" % data)


def innerSql(key, segement, Janpanesechrome, lenth, R_dwarf_virus):
	"""
	params: 
	key:JanpaneseRice_R_dwarf_virus;
	segement:element in count[0];
	lenth:len(count[0])

	return :None
	"""
	sql = "INSERT INTO Rice_chrome_virus ( JanpaneseRice_R_dwarf_virus,  segement, Janpanesechrome, lenth, R_dwarf_virus) VALUES (%s, %s, %s, %s, %s)"
	
	val = (key, segement, Janpanesechrome, lenth, R_dwarf_virus)
	# val = ('Macoo',20)
	print('emm begin')
	try:      

		cursor.execute(sql,val)
		# print()
#         # 提交到数据库执行
		db.commit()
		print('finished this sql sentence')
	except:
		traceback.print_exc()
		# print('finished this sql sentence')
#         # Rollback in case there is any error
		db.rollback()


# if __name__ == '__main__':
#     innerSql()










   
