#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module implementing mainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature, QUrl
from PyQt4 import QtWebKit
from PyQt4 import QtCore, QtGui


from ui.Ui_main_window import Ui_mainWindow

class mainWindow(QMainWindow, Ui_mainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("QString")
    def on_tabWidget_selected(self, p0):
        """
        Slot documentation goes here.
        """
	
        #self.sys_info_view.setUrl(QUrl("file:///home/boss/py/resources/system-info.html"))
        #print "navin patidar"
        # TODO: not implemented yet
        #raise NotImplementedError
    
    @pyqtSignature("QPoint")
    def on_sys_info_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("QPoint")
    def on_sys_info_view_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = mainWindow()
    ui.show()
    sys.exit(app.exec_())
