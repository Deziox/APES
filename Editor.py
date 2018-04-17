# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyaudio
import wave
import UiTeste
import time
import threading as thread

import GraphAmp


class Ui_Editor(object):

    def playOrig(self):
        print("te2")
        try:
            p = pyaudio.PyAudio()
            f = wave.open(r'' + (self.file_name),"rb")
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)

            data = f.readframes(self.CHUNKS)
            while data:
                stream.write(data)
                data = f.readframes(self.CHUNKS)

            stream.stop_stream()
            stream.close()

            p.terminate()
        except Exception as e:
            print(e)

    def ampGraph(self):
        try:
            g = GraphAmp.GraphAmp()
            g.show()
            # AmpGraph.showAmplitudeGraph(path)
        except Exception as e:
            print("test",e)
            time.sleep(7)


    def setupUi(self, EditorWindow):
        file_name = ''
        self.CHUNKS = 1024
        self.file_name = file_name
        print(self.file_name)
        EditorWindow.setObjectName("EditorWindow")
        EditorWindow.resize(878, 698)
        self.centralwidget = QtWidgets.QWidget(EditorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 500, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 330, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(610, 220, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 330, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 210, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 220, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 500, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        image = QtGui.QImage('C:/Users/yetski/Pictures/apesback.jpg')
        sImage = image.scaled(QtCore.QSize(878, 698))
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(sImage))
        EditorWindow.setPalette(palette)
        EditorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EditorWindow)
        self.statusbar.setObjectName("statusbar")
        EditorWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.playOrig)
        self.pushButton_9.clicked.connect(self.ampGraph)
        # self.pushButton_2.clicked.connect(AmpGraph.showAmplitudeGraph())

        self.retranslateUi(EditorWindow)
        QtCore.QMetaObject.connectSlotsByName(EditorWindow)

    def retranslateUi(self, EditorWindow):
        _translate = QtCore.QCoreApplication.translate
        EditorWindow.setWindowTitle(_translate("EditorWindow", "EditorWindow"))
        self.pushButton.setText(_translate("EditorWindow", "Play Original Sound"))

        self.pushButton_7.setText(_translate("EditorWindow", "Effect6"))
        self.pushButton_8.setText(_translate("EditorWindow", "Effect5"))
        self.pushButton_5.setText(_translate("EditorWindow", "Effect3"))
        self.pushButton_9.setText(_translate("EditorWindow", "Show Amplitude Graph"))

        self.pushButton_4.setText(_translate("EditorWindow", "Reverb"))
        self.pushButton_2.setText(_translate("EditorWindow", "Play Edited Sound"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorWindow = QtWidgets.QMainWindow()
    ui = Ui_Editor()
    ui.setupUi(EditorWindow)
    EditorWindow.show()
    sys.exit(app.exec_())

