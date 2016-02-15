# -*- coding: UTF-8 -*-

import xlrd
import MySQLdb
from prettytable import from_db_cursor
import random
random.seed(0)

# variables
host = "127.0.0.1"
user = "admin"
pwd = "password"
dbName = "HardDisk"
tableName = "Components"

# login
db = MySQLdb.connect(host, user, pwd, dbName)
curs=db.cursor()
curs.execute("SET NAMES utf8");

# recreate the table
try:
    curs.execute (""" DROP TABLE %s""" % tableName)
except:
    print "%s does not exist" % tableName
    
curs.execute ("""
    CREATE TABLE %s ( 
        名称 VARCHAR(100),
        型号 VARCHAR(100), 
        封装 VARCHAR(100), 
        数量 INT,
        X INT,
        Y INT,
        Z INT
        
    ) 
    """ % tableName)

# import data from .xls

# xlrd.Book.encoding = "utf-8"
xlsfile = r".\testData.xls" #unicode编码的文字
xlsfile.encode('utf-8') #转换成utf-8格式
book = xlrd.open_workbook(xlsfile,'r')
sheet=book.sheet_by_index(0)     #通过sheet索引获得sheet对象
nrows = sheet.nrows # 获取总行数
# 生产插入的数据
values=[]
for r in range(5,nrows):
    row_data = sheet.row_values(r)   #获得第i行的数据列表
    # 从Unicode转码为utf-8
    for i in range(len(row_data)):
        if isinstance(row_data[i],unicode):
             row_data[i]=row_data[i].encode("utf-8")
    row_data = row_data[:3] +[random.randint(1,10),
                              random.randint(1,10),
                              random.randint(1,10),
                              random.randint(1,10)]
    values.append(row_data)  

#插入多条记录
curs.execute("SET NAMES utf8");
try:
    curs.executemany("INSERT INTO %s" % tableName +
                 "(名称,型号,封装,数量,X,Y,Z)" +
                 "values(%s, %s, %s, %s, %s, %s, %s)",
                 values);
    db.commit()
    print "Data committed"
except:
    db.rollback()
    print "Error: the database is being rolled back"


# output
curs.execute (""" SELECT 名称,型号,数量,X,Y,Z FROM %s """ % tableName)
mytable = from_db_cursor(curs)
print mytable

# close
curs.close()
db.close() 
