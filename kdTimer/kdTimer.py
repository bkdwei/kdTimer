'''
Created on 2019年5月7日

@author: bkd
'''
import sys
import optparse
from os import walk,listdir
from os.path import expanduser,dirname,join,splitext,basename
from PyQt5.QtGui import QTextCursor, QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QWidget,QApplication,QFileDialog, QMessageBox,\
    QMainWindow
from .kdTimer_ui import Ui_MainWindow

class kdTimer(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
def main():
    app = QApplication(sys.argv)
    win = kdTimer()
    win.show()
    sys.exit(app.exec_())        