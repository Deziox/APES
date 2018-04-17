# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Editor import Ui_Editor
import Record
import LivePlot
from multiprocessing import Process
import queue
import threading as thread
import time

class Ui_OtherWindow(object):


    def rec(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            self.pushButton.setText(_translate("OtherWindow", "Recording.."))
            self.sample_width = Record.record()
            self.pushButton.setText(_translate("OtherWindow", "Done Recording"))
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Editor()
            self.ui.setupUi(self.window)

            # OtherWindow.hide()
            self.window.show()
            self.pushButton.setText(_translate("OtherWindow", "Record"))
        except Exception as e:
            print(e)

    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(878, 698)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 410, 521, 171))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 160, 686, 246))
        image = QtGui.QImage('C:/Users/yetski/Pictures/apesback.jpg')
        sImage = image.scaled(QtCore.QSize(878, 698))
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(sImage))
        OtherWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.rec)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        '''
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
        self.label.setText(_translate("OtherWindow", "Welcome To This Window"))
        '''
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
        self.pushButton.setText(_translate("OtherWindow", "Record"))
        self.label.setText(
            _translate("OtherWindow", "Press record to record a new Sample, make sure your microphone is  \n"
                                     "connected. The Recording algorithm will start recording when it hears a sound \n"
                                     "louder than a threshold and will stop after it doesn\'t hear  \n"
                                     "a sound after hearing a sound or if about 10 seconds \n"
                                     "have passed."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
