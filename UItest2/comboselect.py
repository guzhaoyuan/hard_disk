# -*- coding: utf-8 -*-

  # Form implementation generated from reading ui file 'comboselect.ui'
  #
  # Created: Tue Jan 13 20:05:13 2015
  #      by: PyQt4 UI code generator 4.10.3
  #
  # WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
try:
     _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
           return s

try:
     _encoding = QtGui.QApplication.UnicodeUTF8
     def _translate(context, text, disambig):
         return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
     def _translate(context, text, disambig):
         return QtGui.QApplication.translate(context, text, disambig)

class Ui_select(object):
    def setupUi(self, select):
         select.setObjectName(_fromUtf8("select"))
       #  select.resize(460, 232)
         screen = QtGui.QDesktopWidget().screenGeometry()  #解决全屏显示问题
         select.resize(screen.width(), screen.height())

         self.groupBox_pro_city = QtGui.QGroupBox(select)
         self.groupBox_pro_city.setGeometry(QtCore.QRect(30, 30, 401,95 ))
         self.groupBox_pro_city.setObjectName(_fromUtf8("groupBox_pro_city"))
         self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_pro_city)
         self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 101))
         self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
         self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
         self.horizontalLayout.setMargin(0)
         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
         self.label_province = QtGui.QLabel(self.horizontalLayoutWidget)
         self.label_province.setObjectName(_fromUtf8("label_province"))
         self.horizontalLayout.addWidget(self.label_province)
         self.comboBox_province = QtGui.QComboBox(self.horizontalLayoutWidget)
         self.comboBox_province.setObjectName(_fromUtf8("comboBox_province"))
         self.comboBox_province.addItem(_fromUtf8(""))
         self.comboBox_province.addItem(_fromUtf8(""))
         self.comboBox_province.addItem(_fromUtf8(""))
         self.horizontalLayout.addWidget(self.comboBox_province)
         self.label_city = QtGui.QLabel(self.horizontalLayoutWidget)
         self.label_city.setObjectName(_fromUtf8("label_city"))
         self.horizontalLayout.addWidget(self.label_city)
         self.comboBox_city = QtGui.QComboBox(self.horizontalLayoutWidget)
         self.comboBox_city.setObjectName(_fromUtf8("comboBox_city"))
         self.comboBox_city.addItem(_fromUtf8(""))
         self.horizontalLayout.addWidget(self.comboBox_city)
         self.label_town = QtGui.QLabel(self.horizontalLayoutWidget)
         self.label_town.setObjectName(_fromUtf8("label_town"))
         self.horizontalLayout.addWidget(self.label_town)
         self.comboBox_town = QtGui.QComboBox(self.horizontalLayoutWidget)
         self.comboBox_town.setObjectName(_fromUtf8("comboBox_town"))
         self.comboBox_town.addItem(_fromUtf8(""))
         self.horizontalLayout.addWidget(self.comboBox_town)
         self.pushButton_ok = QtGui.QPushButton(select)
         self.pushButton_ok.setGeometry(QtCore.QRect(350, 180, 75, 23))
         self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))

         self.retranslateUi(select)
         QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
         select.setWindowTitle(_translate("select", "Form", None))
         self.groupBox_pro_city.setTitle(_translate("select", "选择器件", None))
         self.label_province.setText(_translate("select", "元件", None))
         self.comboBox_province.setItemText(0, _translate("select", "请选择", None))
         self.comboBox_province.setItemText(1, _translate("select", "电阻", None))
         self.comboBox_province.setItemText(2, _translate("select", "电容", None))
         self.label_city.setText(_translate("select", "型号：", None))
         self.comboBox_city.setItemText(0, _translate("select", "请选择", None))
         self.label_town.setText(_translate("select", "参数：", None))
         self.comboBox_town.setItemText(0, _translate("select", "请选择", None))
         self.pushButton_ok.setText(_translate("select", "确定", None))


if __name__ == "__main__":
     import sys
     app = QtGui.QApplication(sys.argv)
     select = QtGui.QWidget()
     ui = Ui_select()
     ui.setupUi(select)
     select.show()
     sys.exit(app.exec_())