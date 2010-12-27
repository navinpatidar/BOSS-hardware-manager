#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module implementing mainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
from xml_parser import xml_parser
from backend import hw_info_in_xml


from ui.Ui_main_window import Ui_mainWindow

class mainWindow(QMainWindow, Ui_mainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        hw_info_in_xml()
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        hw_info=xml_parser("./resources/hw.xml")
        stack=[hw_info.first_node_key]
        hw_info=hw_info.hw_info
        stack1 = [self.treeWidget]
        while len(stack)!=0 :
            t=stack.pop()
            try:
              hw_info[t]["description"]
            except KeyError :
              try:
                  t=stack.pop()
              except  IndexError:
                  pass
            item = QtGui.QTreeWidgetItem(stack1.pop())
            item.setData(1, 1, list(t))
            #print list(t)
            #for i in item.data(1, 1).toList() :
                #print i.toString()
            try:
                item.setText(0, hw_info[t]["description"])
            except KeyError :
                pass
            tmp=hw_info[t]['child_nodes']
            tmp.reverse()
            for i in tmp:
                stack.append(i) 
                stack1.append(item) 
       #self.sys_info_view.setUrl(QUrl("file:///home/boss/py/resources/system-info.html"))
        self.treeWidget.show()
        
    
    @pyqtSignature("int")
    def on_qt_tabwidget_tabbar_selected(self, p0):
        """
        Slot documentation goes here.
        """
<<<<<<< HEAD
        if p0==0:
             hw_info_in_xml()
=======
	
        #self.sys_info_view.setUrl(QUrl("file:///home/boss/py/resources/system-info.html"))
        #print "navin patidar"
        # TODO: not implemented yet
        #raise NotImplementedError
>>>>>>> 45d4cf71f811309a843c810f6a28cba498ab3903
    
        # TODO: not implemented yet
        #raise NotImplementedError
    @pyqtSignature("QTreeWidgetItem*, int")
    def on_treeWidget_itemClicked(self, item, column):
        """
        Slot documentation goes here.
        """
        t=[]
        [t.append(str(i.toString()))for i in item.data(1, 1).toList() ]
        hw_info=xml_parser("./resources/hw.xml").hw_info
        node=hw_info[tuple(t)]
        #print node
        #print dir(self.tableWidget)
        #self.tableWidget.clear()
        row_count=self.tableWidget.rowCount()
        while row_count !=-1:
            self.tableWidget.removeRow(row_count)
            row_count=row_count-1
        row=0
        for i, j in node.iteritems():
            #print i
            #print j
            if i=="configuration" :
                self.tableWidget.insertRow (row)
                item = QtGui.QTableWidgetItem(i+' :')
                self.tableWidget.setItem(row, 0, item)
                row=row+1 
                for id, value in j.iteritems():
                    self.tableWidget.insertRow (row)
                    item = QtGui.QTableWidgetItem(id)
                    item1 = QtGui.QTableWidgetItem(value)
                    self.tableWidget.setItem(row, 0, item)
                    self.tableWidget.setItem(row, 1, item1)
                    row=row+1
                    
                
            elif i=="capabilities" :
                self.tableWidget.insertRow (row)
                #print dir(self.tableWidget)
                item = QtGui.QTableWidgetItem(i+' :')
                self.tableWidget.setItem(row, 0, item)
                row=row+1 
                for k in j: 
                    item1 = QtGui.QTableWidgetItem(k)
                    self.tableWidget.insertRow (row)
                    self.tableWidget.setItem(row, 1, item1)
                    row+=1
            elif i=="resources" :
                self.tableWidget.insertRow (row)
                item = QtGui.QTableWidgetItem(i+' :')
                self.tableWidget.setItem(row, 0, item)
                row=row+1 
                for id, value in j.iteritems():
                    self.tableWidget.insertRow (row)
                    item = QtGui.QTableWidgetItem(id)
                    item1 = QtGui.QTableWidgetItem(value)
                    self.tableWidget.setItem(row, 0, item)
                    self.tableWidget.setItem(row, 1, item1)
                    row=row+1
            elif i=="child_nodes" :
                pass
            else :
                self.tableWidget.insertRow (row)
                item = QtGui.QTableWidgetItem(i)
                item1 = QtGui.QTableWidgetItem(j)
                self.tableWidget.setItem(row, 0, item)
                self.tableWidget.setItem(row, 1, item1)
                row=row+1
        
       
       

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
