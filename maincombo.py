# -*- coding: utf-8 -*-
# 省市区县联动
# 部分代码来自http://www.lxway.com/46202256.htm

"""
QtGui.QComboBox控件常用函数：
.addItem(string) #添加字符串项到Item
.addItems(list)  #添加列表或元组元素到Item
.clear()  #清除所有Item
.clearEditText() #清除编辑框内容
.count()  #返回Item数目
.currentIndex()  #返回当前选择索引，从0开始
.currentText()  #返回当前选择内容
.insertItem(index,string) #插入字符串项到Item项index后
.insertItems(index,list)  #插入列表或元组元素到Item项index后
.insertSeparator(index)  #插入分隔符到Item项index后
.itemText(index)  #返回Item项index的内容
.removeItem(index)  #删除Item项index
.setCurrentIndex(index)  #设置Item项index为当前选择
.setEditable(True)  #设置选框可编辑
.setEditText(string)  #设置编辑框内容
.setItemText(index,string)  #设置Item项index内容为字符串值
"""

import sys
import time
import serial
import threading
from comboselect import Ui_select
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
import Db

# global constant
port_name = "COM11"

# global variables
executing_flag = 0
port_flag = 0
ser = []


class combosel(QtGui.QWidget):

    def barCodeListener(self):
        past = []
        while 1:
           #  self.ui_sel.lineEdit.setFocus()
            if past != self.ui_sel.lineEdit.text():
                past = self.ui_sel.lineEdit.text()
                print past
                global executing_flag
                executing_flag = 0
            try:
                time.sleep(0.3)
            except:
                continue

    def echoThread(self):
        while port_flag:
            while ser.inWaiting():
                data = ord(ser.read(1))
                print data
                time.sleep(0.1)

    def __init__(self):
        super(combosel, self).__init__()
        self.ui_sel = Ui_select()
        self.ui_sel.setupUi(self)
        self.setWindowTitle(QtCore.QString.fromUtf8("实体硬盘"))

        self.ui_sel.comboBox_borrow_type.clear()  # 清空items
        self.ui_sel.pushButton_borrow_ok.hide()
        self.ui_sel.comboBox_borrow_type.addItem(u'请选择')
        
        self.ui_sel.comboBox_return_type.clear()  # 清空items
        self.ui_sel.pushButton_return_ok.hide()
        self.ui_sel.comboBox_return_type.addItem(u'请选择')


        # 初始化串口
        global ser, port_flag
        try:
            ser = serial.Serial(port_name, 115200)
            port_flag = 1
        except:
            print "Serial Port Failed!"
        t1 = threading.Thread(target=self.echoThread)
        t1.setDaemon(True)
        t1.start()

        # init listener
        # t2 = threading.Thread(target=self.barCodeListener)
        # t2.setDaemon(True)
        # t2.start()

        # 刷新数据库
        Db.Demo()

        # 初始化元件列表
        Db.openDB()
        self.dictType = Db.loadType(1)
        if not self.dictType == None:
            for result in self.dictType:
                self.ui_sel.comboBox_borrow_type.addItem(unicode(result[0], 'utf-8'))

        self.dictType = Db.loadType(0)
        if not self.dictType == None:
            for result in self.dictType:
                self.ui_sel.comboBox_return_type.addItem(unicode(result[0], 'utf-8'))


        # 触发事件
        QtGui.QWidget.connect(self.ui_sel.comboBox_borrow_type, QtCore.SIGNAL('activated(int)'), self.onActivatedBorrow)
        QtGui.QWidget.connect(self.ui_sel.comboBox_borrow_model, QtCore.SIGNAL('activated(int)'), self.onActivatedBorrowParameter)
        QtGui.QWidget.connect(self.ui_sel.comboBox_borrow_parameter, QtCore.SIGNAL('activated(int)'),
                              self.onActivatedShowBorrowbtn)
        QtGui.QWidget.connect(self.ui_sel.pushButton_borrow_ok, QtCore.SIGNAL('clicked()'), self.showborrowmsg)
        
        QtGui.QWidget.connect(self.ui_sel.comboBox_return_type, QtCore.SIGNAL('activated(int)'), self.onActivatedReturn)
        QtGui.QWidget.connect(self.ui_sel.comboBox_return_model, QtCore.SIGNAL('activated(int)'), self.onActivatedReturnParameter)
        QtGui.QWidget.connect(self.ui_sel.comboBox_return_parameter, QtCore.SIGNAL('activated(int)'),
                              self.onActivatedShowReturnbtn)
        QtGui.QWidget.connect(self.ui_sel.pushButton_return_ok, QtCore.SIGNAL('clicked()'), self.showreturnmsg)


    def closeEvent(self, QCloseEvent):
        super(combosel, self).closeEvent(QCloseEvent)
        if port_flag:
            ser.close()
        Db.closeDB()

    # borrow group
    def onActivatedBorrow(self, cuindex):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        if cuindex == 0:
            self.onActivatedBorrowModel(0)
        else:
            type = self.ui_sel.comboBox_borrow_type.currentText()  # Qstring类
            type = type.toUtf8()
            self.onActivatedBorrowModel(type)
        self.ui_sel.pushButton_borrow_ok.hide()

    # 省市联动城市列表
    def onActivatedBorrowModel(self, cuindex):

        self.ui_sel.comboBox_borrow_model.clear()
        self.ui_sel.comboBox_borrow_model.addItem(u'请选择')
        self.ui_sel.comboBox_borrow_parameter.clear()
        self.ui_sel.comboBox_borrow_parameter.addItem(u'请选择')

        if not isinstance(cuindex, int):
            self.dictModel = Db.loadModel(cuindex, 1)
            if not self.dictModel == None:
                for result in self.dictModel:
                    self.ui_sel.comboBox_borrow_model.addItem(unicode(result[0], 'utf-8'))

    # 城市联动区县列表
    def onActivatedBorrowParameter(self, scuindex):
        self.ui_sel.comboBox_borrow_parameter.clear()
        self.ui_sel.comboBox_borrow_parameter.addItem(u'请选择')
        if scuindex:
            type = self.ui_sel.comboBox_borrow_type.currentText().toUtf8()
            model = self.ui_sel.comboBox_borrow_model.currentText().toUtf8()
            self.dictParameter = Db.loadParameter(type, model, 1)
            if not self.dictParameter == None:
                for result in self.dictParameter:
                    self.ui_sel.comboBox_borrow_parameter.addItem(unicode(result[0], 'utf-8'))
        else:
            self.ui_sel.pushButton_borrow_ok.hide()

    # 选择区县效果
    def onActivatedShowBorrowbtn(self, paraindex):
        if paraindex:
            # 区县联动出后可显示button按钮
            self.ui_sel.pushButton_borrow_ok.show()
        else:
            self.ui_sel.pushButton_borrow_ok.hide()

    def showborrowmsg(self):
        global executing_flag
        if executing_flag:
            QtGui.QMessageBox.information(self, (u'提示'), (u'操作未完成!'), QtGui.QMessageBox.Ok)
            return
        type_name = self.ui_sel.comboBox_borrow_type.currentText()
        model_name = self.ui_sel.comboBox_borrow_model.currentText()
        parameter_name = self.ui_sel.comboBox_borrow_parameter.currentText()
        reload(sys)
        sys.setdefaultencoding("utf-8")
        msg = type_name + model_name + parameter_name
        reply = QtGui.QMessageBox.information(self, (u'提示'), (u'确认借出？\n' + msg), QtGui.QMessageBox.Yes |
                                              QtGui.QMessageBox.No)
        if reply == 16384:
            self.borrowComponent(type_name, model_name, parameter_name)
        print reply

    # Return Group
    def onActivatedReturn(self, cuindex):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        if cuindex == 0:
            self.onActivatedReturnModel(0)
        else:
            type = self.ui_sel.comboBox_return_type.currentText()  # Qstring类
            type = type.toUtf8()
            self.onActivatedReturnModel(type)
        self.ui_sel.pushButton_return_ok.hide()

    # 省市联动城市列表
    def onActivatedReturnModel(self, cuindex):

        self.ui_sel.comboBox_return_model.clear()
        self.ui_sel.comboBox_return_model.addItem(u'请选择')
        self.ui_sel.comboBox_return_parameter.clear()
        self.ui_sel.comboBox_return_parameter.addItem(u'请选择')

        if not isinstance(cuindex, int):
            self.dictModel = Db.loadModel(cuindex, 0)
            if not self.dictModel == None:
                for result in self.dictModel:
                    self.ui_sel.comboBox_return_model.addItem(unicode(result[0], 'utf-8'))

    # 城市联动区县列表
    def onActivatedReturnParameter(self, scuindex):
        self.ui_sel.comboBox_return_parameter.clear()
        self.ui_sel.comboBox_return_parameter.addItem(u'请选择')
        if scuindex:
            type = self.ui_sel.comboBox_return_type.currentText().toUtf8()
            model = self.ui_sel.comboBox_return_model.currentText().toUtf8()
            self.dictParameter = Db.loadParameter(type, model, 0)
            if not self.dictParameter == None:
                for result in self.dictParameter:
                    self.ui_sel.comboBox_return_parameter.addItem(unicode(result[0], 'utf-8'))
        else:
            self.ui_sel.pushButton_return_ok.hide()

    # 选择区县效果
    def onActivatedShowReturnbtn(self, paraindex):
        if paraindex:
            # 区县联动出后可显示button按钮
            self.ui_sel.pushButton_return_ok.show()
        else:
            self.ui_sel.pushButton_return_ok.hide()

    def showreturnmsg(self):
        global executing_flag
        if executing_flag:
            QtGui.QMessageBox.information(self, (u'提示'), (u'操作未完成!'), QtGui.QMessageBox.Ok)
            return
        type_name = self.ui_sel.comboBox_return_type.currentText()
        model_name = self.ui_sel.comboBox_return_model.currentText()
        parameter_name = self.ui_sel.comboBox_return_parameter.currentText()
        reload(sys)
        sys.setdefaultencoding("utf-8")
        msg = type_name + model_name + parameter_name
        reply = QtGui.QMessageBox.information(self, (u'提示'), (u'确认归还？\n' + msg), QtGui.QMessageBox.Yes |
                                              QtGui.QMessageBox.No)
        print reply

    def borrowComponent(self, type, model, parameter):
        global executing_flag
        if Db.checkOutRecord(type, model, parameter):
            self.refresh()
            executing_flag = 1
            # send command here
            # command = "\x89\x45\x56"
            # ser.write(command)
        return

    def returnComponent(self, type, model, parameter):
        global executing_flag
        if Db.checkInRecord(type, model, parameter):
            self.refresh()
            executing_flag = 1
            # send command here

    def refresh(self):
        self.onActivatedBorrowModel(0)
        self.onActivatedReturnModel(0)
        self.ui_sel.comboBox_borrow_type.clear()  # 清空items
        self.ui_sel.pushButton_borrow_ok.hide()
        self.ui_sel.comboBox_borrow_type.addItem(u'请选择')
        self.ui_sel.comboBox_return_type.clear()  # 清空items
        self.ui_sel.pushButton_return_ok.hide()
        self.ui_sel.comboBox_return_type.addItem(u'请选择')
        self.dictType = Db.loadType(1)
        if not self.dictType == None:
            for result in self.dictType:
                self.ui_sel.comboBox_borrow_type.addItem(unicode(result[0], 'utf-8'))
        self.dictType = Db.loadType(0)
        if not self.dictType == None:
            for result in self.dictType:
                self.ui_sel.comboBox_return_type.addItem(unicode(result[0], 'utf-8'))
        return


app = QtGui.QApplication(sys.argv)
Appcombosel = combosel()
Appcombosel.show()
sys.exit(app.exec_())
