# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from array import array
import pyaudio
import wave
import time
import threading as thread
import math

import numpy as np

import GraphAmp
from struct import pack

class Ui_Editor(object):

    CHUNKS = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100  # or less so my laptop can keep running
    THRESH = 500
    STEREO = False

    def __init__(self):
        self.graphamp = GraphAmp.GraphAmp()

    def normalize(self,data, MAX=16384):
        x = float(MAX) / max(abs(i) for i in data)

        ret = array('h')
        for i in data:
            ret.append(int(i * x))
        return ret

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

    def playEdit(self):
        print("te2")
        try:
            p = pyaudio.PyAudio()
            f = wave.open(r'' + (self.edit_name),"rb")
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
           self.graphamp.show_plot()
        except Exception as e:
            print("test",e)
            time.sleep(7)

    def tubeDistort(self):
        try:
            p = pyaudio.PyAudio()
            sample_width = p.get_sample_size(self.FORMAT)
            f = open("C:/Users/yetski/Music/Recordings/Raw.txt", "r").read()
            raw = f.split('\n')
            raw.pop()
            raw = [int(i) for i in raw]
            raw = self.fbdistort(raw)
            # sample_width =
            data = pack('<' + ('h' * len(raw)), *raw)
            print(data)
            with wave.open(self.edit_name, 'wb') as wf:
                wf.setnchannels((2 if self.STEREO else 1))
                wf.setsampwidth(sample_width)
                wf.setframerate(self.RATE)
                wf.writeframes(data)
                wf.close()
        except Exception as e:
            print(e)

    def fbdistort(self,raw, thresh=THRESH):
        for i in range(len(raw)):
            '''if(i > thresh or i < -thresh):
                raw[i] = abs(abs(divmod(raw[i] - thresh,thresh*4)[1]) - thresh*2)'''
            if raw[i] > 0:
                raw[i] = int((1 - math.exp(-raw[i])) * 50)
            else:
                raw[i] = int((math.exp(raw[i]) - 1) * 50)

        return self.normalize(raw, 13500)

    def effect2(self):
        try:
            p = pyaudio.PyAudio()
            sample_width = p.get_sample_size(self.FORMAT)
            f = open("C:/Users/yetski/Music/Recordings/Raw.txt", "r").read()
            raw = f.split('\n')
            raw.pop()
            raw = [int(math.fabs(int(i))) for i in raw]

            # sample_width =
            data = pack('<' + ('h' * len(raw)), *raw)
            print(data)
            with wave.open(self.edit_name, 'wb') as wf:
                wf.setnchannels((2 if self.STEREO else 1))
                wf.setsampwidth(sample_width)
                wf.setframerate(self.RATE)
                wf.writeframes(data)
                wf.close()
        except Exception as e:
            print(e)

    def effect3(self):
        try:
            p = pyaudio.PyAudio()
            sample_width = p.get_sample_size(self.FORMAT)
            f = open("C:/Users/yetski/Music/Recordings/Raw.txt", "r").read()
            raw = f.split('\n')
            raw.pop()
            print(''.join(raw))
            raw = [int(i) for i in raw]
            raw.reverse()
            print(''.join([str(i) for i in raw]))
            # sample_width =
            data = pack('<' + ('h' * len(raw)), *raw)
            with wave.open(self.edit_name, 'wb') as wf:
                wf.setnchannels((2 if self.STEREO else 1))
                wf.setsampwidth(sample_width)
                wf.setframerate(self.RATE)
                wf.writeframes(data)
                wf.close()
        except Exception as e:
            print(e)

    def effect4(self):
        try:
            wr = wave.open(self.file_name, 'r')
            # Set the parameters for the output file.
            par = list(wr.getparams())
            par[3] = 0  # The number of samples will be set by writeframes.
            par = tuple(par)
            ww = wave.open(self.edit_name, 'w')
            ww.setparams(par)

            fr = 20
            sz = wr.getframerate() // fr  # Read and process 1/fr second at a time.
            # A larger number for fr means less reverb.
            c = int(wr.getnframes() / sz)  # count of the whole file
            shift = 200 // fr  # shifting 200 Hz
            for num in range(c):
                da = np.fromstring(wr.readframes(sz), dtype=np.int16)
                left, right = da[0::2], da[1::2]  # left and right channel
                lf, rf = np.fft.rfft(left), np.fft.rfft(right)
                lf, rf = np.roll(lf, shift), np.roll(rf, shift)
                lf[0:shift], rf[0:shift] = 0, 0
                nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
                ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
                ww.writeframes(ns.tostring())
            wr.close()
            ww.close()
        except Exception as e:
            print(e)


    def setupUi(self, EditorWindow,file_name = 'C:/Users/yetski/Music/Recordings/Recording.wav',edit_name = 'C:/Users/yetski/Music/Recordings/Recording2.wav'):
        # file_name = 'C:/Users/yetski/Music/Recordings/Recording.wav'
        self.CHUNKS = 1024
        self.file_name = file_name
        self.edit_name = edit_name
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
        self.pushButton_2.clicked.connect(self.playEdit)
        self.pushButton_4.clicked.connect(self.tubeDistort)
        self.pushButton_5.clicked.connect(self.effect2)
        self.pushButton_8.clicked.connect(self.effect3)
        self.pushButton_7.clicked.connect(self.effect4)
        # self.pushButton_2.clicked.connect(AmpGraph.showAmplitudeGraph())

        self.retranslateUi(EditorWindow)
        QtCore.QMetaObject.connectSlotsByName(EditorWindow)

    def retranslateUi(self, EditorWindow):
        _translate = QtCore.QCoreApplication.translate
        EditorWindow.setWindowTitle(_translate("EditorWindow", "EditorWindow"))
        self.pushButton.setText(_translate("EditorWindow", "Play Original Sound"))

        self.pushButton_7.setText(_translate("EditorWindow", "Pitch Shift"))
        self.pushButton_8.setText(_translate("EditorWindow", "Reverse"))
        self.pushButton_5.setText(_translate("EditorWindow", "Abs val bits"))
        self.pushButton_9.setText(_translate("EditorWindow", "Show Amplitude Graph"))

        self.pushButton_4.setText(_translate("EditorWindow", "Tube Distort"))
        self.pushButton_2.setText(_translate("EditorWindow", "Play Edited Sound"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorWindow = QtWidgets.QMainWindow()
    ui = Ui_Editor()
    ui.setupUi(EditorWindow)
    EditorWindow.show()
    sys.exit(app.exec_())

