# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from OtherWindow import Ui_OtherWindow
from Editor import Ui_Editor
from LoadSound import App
import time

class Ui_MainWindow(object):

    def openWindow(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OtherWindow()
            self.ui.setupUi(self.window)
            # MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(e)

    def loadWindow(self):
        # self.file_name = QFileDialog.show()
        try:
            load = App()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Editor()
            print(self.ui)
            self.ui.setupUi(self.window,load.getFileName())
            self.window.show()
        except Exception as e:
            print('test',e)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 180, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 330, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 490, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 490, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        image = QtGui.QImage('C:/Users/yetski/Pictures/apesback.jpg')
        sImage = image.scaled(QtCore.QSize(878, 698))
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(sImage))
        MainWindow.setPalette(palette)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(216, 12, 411, 151))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        pixmap = QtGui.QPixmap('A.P.E.S..png')
        self.label_2.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(0, 0, 881, 671))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_2.raise_()

        icon = QtGui.QIcon()
        icon.addFile('C:/Users/yetski/Pictures/ape.png', QtCore.QSize(64, 64))
        MainWindow.setWindowIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2.clicked.connect(self.loadWindow)
    
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''_translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open.setText(_translate("MainWindow", "Open Window"))
        self.label.setText(_translate("MainWindow", "Click To Open Window"))'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "New Sound"))
        self.pushButton_2.setText(_translate("MainWindow", "Load Sound"))
        self.pushButton_3.setText(_translate("MainWindow", "Settings"))
        self.pushButton_4.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


