'''
Created on 2019年5月7日

@author: bkd
'''
import sys
import optparse
import time
from os import walk,listdir
from os.path import expanduser,dirname,join,splitext,basename
from PyQt5.QtGui import QTextCursor, QIcon
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot,QDate
from PyQt5.QtWidgets import  QWidget,QApplication,QFileDialog, QMessageBox,\
    QMainWindow
import pickle
from .kdTimer_ui import Ui_MainWindow
from .fileutil import check_and_create,get_file_realpath
from .exception_handler import global_exception_hander

class kdTimer(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.exception_handler = global_exception_hander()
        self.exception_handler.patch_excepthook()
        
        self.config_file =join(expanduser('~') , ".config/kdTimer/profile.dat")
        check_and_create(self.config_file)
        
        self.load_event_times()
        self.lw_event.currentItemChanged.connect(self.on_lw_event_currentItemChanged)
        self.list_pending_flag = False
#         self.event_timers = []
    
    #新增
    @pyqtSlot()
    def on_pb_add_clicked(self):
        self.cur_event = None
        self.le_event.clear()
        now_day = time.strftime("%Y-%m-%d", time.localtime())
        self.de_dead_date.setDate(QDate.fromString(now_day, 'yyyy-MM-dd'))
    #保存
    @pyqtSlot()
    def on_pb_save_clicked(self):
        event_timer = {}
        event_timer["name"] = self.le_event.text()
        event_timer["dead_date"] = self.de_dead_date.date().toString()
        print(event_timer)
        self.event_timers.append(event_timer)
        with open(self.config_file,"wb") as pf:
            pickle.dump(self.event_timers,pf)
        self.load_event_times()
            
    def load_event_times(self):
        with open(self.config_file,"rb") as pf:
            self.event_timers = pickle.load(pf)
            print("self.event_timers",self.event_timers)
            self.list_pending_flag = True
            self.lw_event.clear()
            for event_timer in self.event_timers :
                self.lw_event.addItem(event_timer["name"])
            self.list_pending_flag = False
    def on_pb_delete_clicked(self):
#         print(self.lw_event.selectedItems(),self.lw_event.count())
        seleted_item = self.cur_event
        for event_timer in self.event_timers :
            if(event_timer["name"] == seleted_item) :
                self.list_pending_flag = True
                self.event_timers.remove(event_timer)
                self.list_pending_flag = False
                print("delete " + seleted_item)
                self.load_event_times()
                break
    @pyqtSlot()
    def on_lw_event_currentItemChanged(self):
        if not self.list_pending_flag :
            print(self.lw_event.currentItem().text())
            self.cur_event  = self.lw_event.currentItem().text()
            
        
        
def main():
    app = QApplication(sys.argv)
    win = kdTimer()
    win.show()
    sys.exit(app.exec_())        