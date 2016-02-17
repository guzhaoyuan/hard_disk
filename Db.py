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
db = []
curs = []


def openDB():
    global db, curs
    try:
        db = MySQLdb.connect(host, user, pwd, dbName)
        curs = db.cursor()
        curs.execute("SET NAMES utf8")
        return True
    except:
        return False


def closeDB():
    try:
        curs.close()
        db.close()
        return True
    except:
        return False


def addRecord(type, model, parameter, x, y, z, status):
    curs.execute("SET NAMES utf8")
    try:
        curs.execute("INSERT INTO %s" % tableName +
                     "(type, model,parameter,X,Y,Z,Status,Ocupied)" +
                     "values(%s, %s, %s, %s, %s, %s, %s, %s)",
                     (type, model, parameter, x, y, z, status, 1)
                     )
        db.commit()
        return True
    except:
        db.rollback()
        return False


def deleteRecord(type, model, parameter):
    return


def checkInRecord(type, model, parameter, x, y, z):
    return


def checkOutRecord(type, model, parameter):
    return


def loadAllRecords():
    curs.execute("SELECT * FROM %s" % tableName)
    return curs.fetchall()


def loadRecords(elType):
    curs.execute("SELECT %s FROM %s" %
                 (elType, tableName))
    return curs.fetchall()


def printTable():
    curs.execute (""" SELECT type,model,parameter FROM %s
            WHERE type = '%s'""" % (tableName, '电阻') )
    print from_db_cursor(curs)


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
                Ocupied INT
            )
            """ % tableName)
        return True
    except:
        return False


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
        row_data = row_data[:3] + [random.randint(1, 10),
                                   random.randint(1, 10),
                                   random.randint(1, 10),
                                   random.randint(0, 1),
                                   random.randint(0, 1)]
        values.append(row_data)
    # 插入多条记录
    curs.execute("SET NAMES utf8")
    try:
        curs.executemany("INSERT INTO %s" % tableName +
                         "(type, model,parameter,X,Y,Z,Status,Ocupied)" +
                         "values(%s, %s, %s, %s, %s, %s, %s, %s)",
                         values);
        db.commit()
        return True
    except:
        db.rollback()
        print False


def demo():
    print 'openDB ' + str(openDB())
    print 'recreateTable ' + str(recreateTable())
    xlsfile = r"./testData.xls"
    print 'loadFile ' + str(loadFile(xlsfile))
    printTable()
    print 'addRecord ' + str(addRecord(
            '电阻', '添加的电阻', '100欧', 3, 4, 5, 1))
    printTable()

    print loadAllRecords()

    print loadRecords("type")

    print loadRecords("model")

    print "closeDB " + str(closeDB())
