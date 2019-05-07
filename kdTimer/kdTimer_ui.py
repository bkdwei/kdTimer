# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bkd/git/kdTimer\kdTimer\kdTimer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_add = QtWidgets.QPushButton(self.centralwidget)
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout.addWidget(self.pb_add)
        self.pb_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout.addWidget(self.pb_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lw_event = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_event.sizePolicy().hasHeightForWidth())
        self.lw_event.setSizePolicy(sizePolicy)
        self.lw_event.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lw_event.setObjectName("lw_event")
        self.verticalLayout.addWidget(self.lw_event)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_event = QtWidgets.QLineEdit(self.centralwidget)
        self.le_event.setObjectName("le_event")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_event)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.de_dead_date = QtWidgets.QDateEdit(self.centralwidget)
        self.de_dead_date.setObjectName("de_dead_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.de_dead_date)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pb_save = QtWidgets.QPushButton(self.centralwidget)
        self.pb_save.setObjectName("pb_save")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pb_save)
        self.lb_rest_days = QtWidgets.QLabel(self.centralwidget)
        self.lb_rest_days.setObjectName("lb_rest_days")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lb_rest_days)
        self.horizontalLayout_2.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_add.setText(_translate("MainWindow", "新增"))
        self.pb_delete.setText(_translate("MainWindow", "删除"))
        self.label.setText(_translate("MainWindow", "事件"))
        self.label_2.setText(_translate("MainWindow", "截止日期"))
        self.label_3.setText(_translate("MainWindow", "剩余天数"))
        self.pb_save.setText(_translate("MainWindow", "保存"))
        self.lb_rest_days.setText(_translate("MainWindow", "0天"))

