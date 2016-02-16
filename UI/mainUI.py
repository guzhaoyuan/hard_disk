#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class DBComboBoxDelegate(QItemDelegate):

  def __init__(self, comboModel, parent=None):
    QItemDelegate.__init__(self, parent)
    self.comboModel = comboModel

  def __createComboView(self, parent):
    view = QTableView(parent)
    view.setModel(self.comboModel)
    view.setAutoScroll(False)
    view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    view.setSelectionMode(QAbstractItemView.SingleSelection)
    view.setSelectionBehavior(QAbstractItemView.SelectRows)
    view.resizeColumnsToContents()
    view.resizeRowsToContents()
    view.setMinimumWidth(view.horizontalHeader().length())
    return view

  def createEditor(self, parent, option, index):
    combo = QComboBox(parent)
    #!! The important part: First set the model, then the view on the combo box
    combo.setModel(self.comboModel)
    #combo.setModelColumn(1)
    combo.setView(self.__createComboView(parent))
    return combo

  def setEditorData(self, editor, index):
    value = index.model().data(index, Qt.EditRole).toString()
    editor.setCurrentIndex(editor.findText(value))

  def setModelData(self, editor, model, index):
    if editor.currentIndex() >= 0:
      realidx = editor.model().index(editor.currentIndex(), 0) #确保取第一列的值
      value = editor.model().data(realidx)
      model.setData(index, value, Qt.EditRole)

###############################################################################

if __name__ == '__main__':
  import sys
  app = QApplication(sys.argv)

  table = QTableView()

  comboModel = QStandardItemModel(4,1 , table)
  comboModel.setHorizontalHeaderLabels(['Name'])
  comboModel.setData(comboModel.index(0, 0, QModelIndex()), QVariant(u'电阻'))
  comboModel.setData(comboModel.index(1, 0, QModelIndex()), QVariant(u'电感'))
  comboModel.setData(comboModel.index(2, 0, QModelIndex()), QVariant(u'电容'))
  comboModel.setData(comboModel.index(3, 0, QModelIndex()), QVariant(u'芯片'))

  model = QStandardItemModel(1, 3, table)
  model.setHorizontalHeaderLabels([u'器件', u'型号', u'参数'])


  table.setModel(model)
  table.setItemDelegateForColumn(0, DBComboBoxDelegate(comboModel, table))
  #table.setItemDelegateForColumn(1,DBComboBoxDelegate(comboModel,table))
  #table.setItemDelegateForColumn(2,DBComboBoxDelegate(comboModel,table))
  table.horizontalHeader().setStretchLastSection(True)
  table.setGeometry(80, 20, 400, 300)
  table.setWindowTitle('Search!')
  table.show()

  sys.exit(app.exec_())