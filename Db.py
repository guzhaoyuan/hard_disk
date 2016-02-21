# -*- coding: UTF-8 -*-

import random
import MySQLdb
import xlrd
from prettytable import from_db_cursor

# for repeatability
random.seed(0)

# variables
host = "127.0.0.1"
user = "admin"
pwd = "password"
dbName = "HardDisk"
tableName = "Components"

max_X = 4
max_Y = 4
max_Z = 2

db = []
curs = []

# 数据表成员
# type
# model
# parameter
# x
# y
# z
# status        1 在架上(未被借出)     0 表示不再架上(被借出)
# occupied      1 该位置被元件占用     0 该位置为空


# 打开数据库
def openDB():
    global db, curs
    try:
        db = MySQLdb.connect(host, user, pwd, dbName)
        curs = db.cursor()
        curs.execute("SET NAMES utf8")
        return True
    except:
        return False


# 关闭数据库
def closeDB():
    try:
        curs.close()
        db.close()
        return True
    except:
        return False


# 添加条目
# 输入：type, model, parameter, x, y, z, status
# 输出：True(成功), False(失败)
def addRecord(type, model, parameter, x, y, z, status):
    curs.execute("SET NAMES utf8")
    try:
        curs.execute("UPDATE %s SET" % tableName +
                     " type = %s, model = %s,parameter = %s,"
                     " status = %s, occupied = 1 "
                     "WHERE X = %s AND Y = %s AND Z = %s",
                     (type, model, parameter, status, x, y, z)
                     )
        db.commit()
        return True
    except:
        db.rollback()
        return False


# 删除条目
# 输入：type, model, parameter
# 输出：True(成功), False(失败)
def deleteRecord(type, model, parameter):
    curs.execute("SET NAMES utf8")
    try:
        curs.execute(" UPDATE %s SET" % tableName +
                     " type = '', model = ''," +
                     " parameter = '', status = 1, " +
                     " occupied = 0 WHERE" +
                     " type = %s AND" +
                     " model = %s AND" +
                     " parameter = %s",
                     (type, model, parameter)
                     )
        db.commit()
        return True
    except:
        db.rollback()
        return False


# 归还元件
# 输入：type, model, parameter
# 输出：True(成功), False(失败)
def checkInRecord(type, model, parameter):
    try:
        curs.execute(" UPDATE %s SET" % tableName +
                     " status = 1 WHERE " +
                     " type = %s AND" +
                     " model = %s AND" +
                     " parameter = %s",
                     (type, model, parameter)
                     )
        db.commit()
        return True
    except:
        db.rollback()
        return False


# 借出元件
# 输入：type, model, parameter
# 输出：True(成功), False(失败)
def checkOutRecord(type, model, parameter):
    try:
        curs.execute(" UPDATE %s SET" % tableName +
                     " status = 0 WHERE " +
                     " type = %s AND" +
                     " model = %s AND" +
                     " parameter = %s",
                     (type, model, parameter)
                     )
        db.commit()
        return True
    except:
        db.rollback()
        return False


# 获取所有数据
# 输出：Tuple
def loadAllRecords():
    curs.execute("SELECT * FROM %s" % tableName)
    return curs.fetchall()


# 获取type
# 输出：Tuple
def loadType():
    curs.execute("SELECT DISTINCT type FROM %s" %
                 tableName)
    return curs.fetchall()


# 获取model
# 输出：Tuple
def loadModel(type):
    curs.execute("SELECT DISTINCT model FROM %s " % tableName +
                 "WHERE type = %s", type)
    return curs.fetchall()


# 获取parameter
# 输出：Tuple
def loadParameter(type, model):
    curs.execute("SELECT parameter FROM %s " % tableName +
                 "WHERE type = %s AND model = %s",
                 (type, model))
    return curs.fetchall()


# 获取坐标
# 输出：Tuple
def getPos(type, model, parameter):
    curs.execute("SELECT X, Y, Z FROM %s " % tableName +
                 "WHERE type = %s AND model = %s AND parameter = %s",
                 (type, model, parameter))
    return curs.fetchone()


# 打印全表
def printTable():
    curs.execute (""" SELECT * FROM %s""" % tableName)
    print from_db_cursor(curs)


# 重新创建表格
def recreateTable():
    try:
        curs.execute(""" DROP TABLE IF EXISTS %s""" % tableName)
        curs.execute("""
            CREATE TABLE %s (
                type VARCHAR(100),
                model VARCHAR(100),
                parameter VARCHAR(100),
                X INT,
                Y INT,
                Z INT,
                Status INT,
                Occupied INT
            )
            """ % tableName)
        for z in range(max_Z):
            for y in range(max_Y):
                for x in range(max_X):
                    curs.execute("INSERT INTO %s" % tableName +
                         "(X,Y,Z,Status,Occupied)" +
                         "values(%s, %s, %s, %s, %s)",
                                 (x, y, z, 1, 0))
        db.commit()
        return True
    except:
        db.rollback()
        return False


# 返回下一个空位
def nextEmpty():
    try:
        curs.execute(" SELECT x, y, z FROM %s"
                     " WHERE occupied = 0" % tableName)
        if curs.rowcount:
            return curs.fetchone()
        else:
            return None
    except:
        db.rollback()
        return None


# 导入测试数据
def loadFile(filename):
    book = xlrd.open_workbook(filename, 'r')
    sheet = book.sheet_by_index(0)  # 通过sheet索引获得sheet对象
    nrows = sheet.nrows  # 获取总行数
    # 生产插入的数据
    values = []
    for r in range(5, nrows):
        row_data = sheet.row_values(r)  # 获得第i行的数据列表
        # 从Unicode转码为utf-8
        for i in range(len(row_data)):
            if isinstance(row_data[i], unicode):
                row_data[i] = row_data[i].encode("utf-8")
        # 获取存储位置
        pos = nextEmpty()
        if pos == None:
            return False
        else:
            if addRecord(row_data[0], row_data[1], row_data[2],
                      pos[0], pos[1], pos[2], 1):
                continue
            else:
                return False
    return True


# Demo 将表格恢复到默认
def Demo():
    openDB()
    recreateTable()
    loadFile(r"./testData.xls")
    printTable()
    closeDB()


# Test 测试接口
def Test():
    openDB()
    result = loadType()
    print '\n', result
    for i in result:
        print i[0]
    result = loadModel("电阻")
    print '\n', result
    for i in result:
        print i[0]
    result = loadParameter('电阻', '碳膜电阻')
    print '\n', result
    for i in result:
        print i[0]
    result = getPos('电阻', '碳膜电阻', '精度5%,1/4W、1/8W')
    print '\n', result
    for i in result:
        print i
    closeDB()
