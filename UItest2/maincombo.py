# -*- coding: utf-8 -*-
#省市区县联动
# 部分代码来自http://www.lxway.com/46202256.htm

'''
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
'''

import  sys
from comboselect import Ui_select
from PyQt4 import QtGui, QtCore
from  PyQt4.QtCore import *
import area
class combosel(QtGui.QWidget):
    def __init__(self):
        super(combosel, self).__init__()
        self.ui_sel = Ui_select()
        self.ui_sel.setupUi(self)
        self.setWindowTitle('Pyqt ComboBox')
        self.setWindowIcon(QtGui.QIcon('../Document/images/QQ.png'))
        # self.ui_sel.comboBox_province.addItem(QtGui.QIcon('../Document/images/favicon.ico'),'sd')   # 添加 qico图标
        self.ui_sel.comboBox_province.clear() # 清空items
        self.dictPorovince = area.dictPorovince
        self.dictCity = area.dictCity
        self.dictTown = area.dicTown
        self.ui_sel.pushButton_ok.hide()
        self.ui_sel.comboBox_province.addItem(u'请选择')
        #初始化省份
        for (keys, val) in self.dictPorovince.items():
            self.ui_sel.comboBox_province.addItem(val, QVariant(keys))

        # 触发事件
        QtGui.QWidget.connect(self.ui_sel.comboBox_province, QtCore.SIGNAL('activated(int)'), self.onActivated)
        QtGui.QWidget.connect(self.ui_sel.comboBox_city, QtCore.SIGNAL('activated(int)'), self.onActivatedTown)
        QtGui.QWidget.connect(self.ui_sel.comboBox_town, QtCore.SIGNAL('activated(int)'), self.onActivatedShowbtn)
        QtGui.QWidget.connect(self.ui_sel.pushButton_ok, QtCore.SIGNAL('clicked()'), self.showmsg)

    def onActivated(self, cuindex):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        intdata=self.ui_sel.comboBox_province.itemData(cuindex)
        # print(intdata.toPyObject())  #也可获取data里面的值, type()==int
        if not isinstance(intdata, str):
            Vintdata = int(intdata.toString())    # type() == string
            self.onActivatedCity(Vintdata)
        self.ui_sel.pushButton_ok.hide()
    # 省市联动城市列表
    def onActivatedCity(self, cuindex):
        self.ui_sel.comboBox_city.clear()
        self.ui_sel.comboBox_city.addItem(u'请选择')
        self.ui_sel.comboBox_town.clear()
        self.ui_sel.comboBox_town.addItem(u'请选择')
        for (keys, val) in self.dictCity[cuindex].items():
            self.ui_sel.comboBox_city.addItem(val, QVariant(keys))
    # 城市联动区县列表
    def onActivatedTown(self, scuindex):
        self.ui_sel.comboBox_town.clear()
        self.ui_sel.comboBox_town.addItem(u'请选择')
        intdata = self.ui_sel.comboBox_city.itemData(scuindex)
        for (keysd, vald) in self.dictTown[intdata.toPyObject()].items():
            self.ui_sel.comboBox_town.addItem(vald, QVariant(keysd))

    # 选择区县效果
    def onActivatedShowbtn(self):
        #区县联动出后可显示button按钮
        self.ui_sel.pushButton_ok.show()


    def showmsg(self):
        province_index = self.ui_sel.comboBox_province.currentIndex()
        city_index = self.ui_sel.comboBox_city.currentIndex()
        town_index = self.ui_sel.comboBox_town.currentIndex()
        province_nid = self.ui_sel.comboBox_province.itemData(province_index)
        province_name = self.ui_sel.comboBox_province.itemText(province_index)
        city_nid = self.ui_sel.comboBox_city.itemData(city_index)
        city_name = self.ui_sel.comboBox_city.itemText(city_index)
        town_nid = self.ui_sel.comboBox_town.itemData(town_index)
        town_name = self.ui_sel.comboBox_town.itemText(town_index)
        reload(sys)
        sys.setdefaultencoding("utf-8")
        msg=province_name+city_name+town_name
        msg_id= str(province_nid.toPyObject())+'+'+str(city_nid.toPyObject())+'+'+str(town_nid.toPyObject())
        print(msg_id)
        QtGui.QMessageBox.information(self, (u'提示'),(u''+msg+', ID:'+msg_id),QtGui.QMessageBox.Yes)

        show_istaking = QtGui.QMessageBox.information(self,(u'提示'),(u'正在取件……'), QtGui.QMessageBox.Yes)
        QObject.connect(QtGui.QMessageBox.Yes,QtCore.SIGNAL("clicked()"),show_istaking)

app=QtGui.QApplication(sys.argv)
Appcombosel = combosel()
Appcombosel.show()
sys.exit(app.exec_())