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
        select.resize(660, 262)
        # screen = QtGui.QDesktopWidget().screenGeometry()  #解决全屏显示问题
        # select.resize(screen.width(), screen.height())

        # Borrow Group
        self.groupBox_pro_borrow = QtGui.QGroupBox(select)
        self.groupBox_pro_borrow.setGeometry(QtCore.QRect(30, 30, 600, 80))
        self.groupBox_pro_borrow.setObjectName(_fromUtf8("groupBox_pro_borrow"))
        self.horizontalLayoutBorrowWidget = QtGui.QWidget(self.groupBox_pro_borrow)
        self.horizontalLayoutBorrowWidget.setGeometry(QtCore.QRect(10, 5, 485, 80))
        self.horizontalLayoutBorrowWidget.setObjectName(_fromUtf8("horizontalLayoutBorrowWidget"))
        self.horizontalLayoutBorrow = QtGui.QHBoxLayout(self.horizontalLayoutBorrowWidget)
        self.horizontalLayoutBorrow.setMargin(0)
        self.horizontalLayoutBorrow.setObjectName(_fromUtf8("horizontalLayoutBorrow"))

        self.label_borrow_type = QtGui.QLabel(self.horizontalLayoutBorrowWidget)
        self.label_borrow_type.setObjectName(_fromUtf8("label_borrow_type"))
        self.horizontalLayoutBorrow.addWidget(self.label_borrow_type)

        self.comboBox_borrow_type = QtGui.QComboBox(self.horizontalLayoutBorrowWidget)
        self.comboBox_borrow_type.setObjectName(_fromUtf8("comboBox_borrow_type"))
        self.comboBox_borrow_type.addItem(_fromUtf8(""))
        self.comboBox_borrow_type.setFixedSize(100, 20)  # setSize
        self.horizontalLayoutBorrow.addWidget(self.comboBox_borrow_type)

        self.label_borrow_model = QtGui.QLabel(self.horizontalLayoutBorrowWidget)
        self.label_borrow_model.setObjectName(_fromUtf8("label_borrow_model"))
        self.horizontalLayoutBorrow.addSpacing(10)
        self.horizontalLayoutBorrow.addWidget(self.label_borrow_model)

        self.comboBox_borrow_model = QtGui.QComboBox(self.horizontalLayoutBorrowWidget)
        self.comboBox_borrow_model.setObjectName(_fromUtf8("comboBox_borrow_model"))
        self.comboBox_borrow_model.addItem(_fromUtf8(""))
        self.comboBox_borrow_model.setFixedSize(100, 20)
        self.horizontalLayoutBorrow.addWidget(self.comboBox_borrow_model)

        self.label_borrow_parameter = QtGui.QLabel(self.horizontalLayoutBorrowWidget)
        self.label_borrow_parameter.setObjectName(_fromUtf8("label_borrow_parameter"))
        self.horizontalLayoutBorrow.addSpacing(10)
        self.horizontalLayoutBorrow.addWidget(self.label_borrow_parameter)

        self.comboBox_borrow_parameter = QtGui.QComboBox(self.horizontalLayoutBorrowWidget)
        self.comboBox_borrow_parameter.setObjectName(_fromUtf8("comboBox_borrow_parameter"))
        self.comboBox_borrow_parameter.addItem(_fromUtf8(""))
        self.comboBox_borrow_parameter.setFixedSize(100, 20)
        self.horizontalLayoutBorrow.addWidget(self.comboBox_borrow_parameter)

        self.pushButton_borrow_ok = QtGui.QPushButton(select)
        self.pushButton_borrow_ok.setGeometry(QtCore.QRect(540, 64, 75, 22))
        self.pushButton_borrow_ok.setObjectName(_fromUtf8("pushButton_borrow_ok"))

        # Return Group
        self.groupBox_pro_return = QtGui.QGroupBox(select)
        self.groupBox_pro_return.setGeometry(QtCore.QRect(30, 130, 600, 80))
        self.groupBox_pro_return.setObjectName(_fromUtf8("groupBox_pro_return"))
        self.horizontalLayoutReturnWidget = QtGui.QWidget(self.groupBox_pro_return)
        self.horizontalLayoutReturnWidget.setGeometry(QtCore.QRect(10, 5, 485, 80))
        self.horizontalLayoutReturnWidget.setObjectName(_fromUtf8("horizontalLayoutReturnWidget"))
        self.horizontalLayoutReturn = QtGui.QHBoxLayout(self.horizontalLayoutReturnWidget)
        self.horizontalLayoutReturn.setMargin(0)
        self.horizontalLayoutReturn.setObjectName(_fromUtf8("horizontalLayoutReturn"))

        self.label_return_type = QtGui.QLabel(self.horizontalLayoutReturnWidget)
        self.label_return_type.setObjectName(_fromUtf8("label_return_type"))
        self.horizontalLayoutReturn.addWidget(self.label_return_type)

        self.comboBox_return_type = QtGui.QComboBox(self.horizontalLayoutReturnWidget)
        self.comboBox_return_type.setObjectName(_fromUtf8("comboBox_return_type"))
        self.comboBox_return_type.addItem(_fromUtf8(""))
        self.comboBox_return_type.setFixedSize(100, 20)  # setSize
        self.horizontalLayoutReturn.addWidget(self.comboBox_return_type)

        self.label_return_model = QtGui.QLabel(self.horizontalLayoutReturnWidget)
        self.label_return_model.setObjectName(_fromUtf8("label_return_model"))
        self.horizontalLayoutReturn.addSpacing(10)
        self.horizontalLayoutReturn.addWidget(self.label_return_model)

        self.comboBox_return_model = QtGui.QComboBox(self.horizontalLayoutReturnWidget)
        self.comboBox_return_model.setObjectName(_fromUtf8("comboBox_return_model"))
        self.comboBox_return_model.addItem(_fromUtf8(""))
        self.comboBox_return_model.setFixedSize(100, 20)
        self.horizontalLayoutReturn.addWidget(self.comboBox_return_model)

        self.label_return_parameter = QtGui.QLabel(self.horizontalLayoutReturnWidget)
        self.label_return_parameter.setObjectName(_fromUtf8("label_return_parameter"))
        self.horizontalLayoutReturn.addSpacing(10)
        self.horizontalLayoutReturn.addWidget(self.label_return_parameter)

        self.comboBox_return_parameter = QtGui.QComboBox(self.horizontalLayoutReturnWidget)
        self.comboBox_return_parameter.setObjectName(_fromUtf8("comboBox_return_parameter"))
        self.comboBox_return_parameter.addItem(_fromUtf8(""))
        self.comboBox_return_parameter.setFixedSize(100, 20)
        self.horizontalLayoutReturn.addWidget(self.comboBox_return_parameter)

        self.pushButton_return_ok = QtGui.QPushButton(select)
        self.pushButton_return_ok.setGeometry(QtCore.QRect(540, 164, 75, 22))
        self.pushButton_return_ok.setObjectName(_fromUtf8("pushButton_return_ok"))

        self.retranslateUi(select)
        QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
        select.setWindowTitle(_translate("select", "Form", None))
        
        self.groupBox_pro_borrow.setTitle(_translate("select", "借出", None))
        self.label_borrow_type.setText(_translate("select", "元件：", None))
        self.comboBox_borrow_type.setItemText(0, _translate("select", "请选择", None))
        self.label_borrow_model.setText(_translate("select", "型号：", None))
        self.comboBox_borrow_model.setItemText(0, _translate("select", "请选择", None))
        self.label_borrow_parameter.setText(_translate("select", "参数：", None))
        self.comboBox_borrow_parameter.setItemText(0, _translate("select", "请选择", None))
        self.pushButton_borrow_ok.setText(_translate("select", "确定", None))

        self.groupBox_pro_return.setTitle(_translate("select", "归还", None))
        self.label_return_type.setText(_translate("select", "元件：", None))
        self.comboBox_return_type.setItemText(0, _translate("select", "请选择", None))
        self.label_return_model.setText(_translate("select", "型号：", None))
        self.comboBox_return_model.setItemText(0, _translate("select", "请选择", None))
        self.label_return_parameter.setText(_translate("select", "参数：", None))
        self.comboBox_return_parameter.setItemText(0, _translate("select", "请选择", None))
        self.pushButton_return_ok.setText(_translate("select", "确定", None))

        self.lineEdit = QtGui.QLineEdit(select)
        self.lineEdit.selectAll()
        self.lineEdit.setFocus()
        # self.lineEdit.setFocusPolicy()
        self.lineEdit.setGeometry(400, 364, 75, 22)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    select = QtGui.QWidget()
    ui = Ui_select()
    ui.setupUi(select)
    select.show()
    sys.exit(app.exec_())
