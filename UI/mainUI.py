#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

#一个窗口类
class Window(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300,300,250,159)

app = QtGui.QApplication(sys.argv)
wel = Window()
wel.setWindowTitle('Welcome!')
wel.show()
button_1 = QtGui.QPushButton('1',wel)
button_1.setGeometry(10,10,60,35)
button_2 = QtGui.QPushButton('2',wel)
button_2.setGeometry(90,10,60,35)
button_1.show()
button_2.show()
sys.exit(app.exec_())