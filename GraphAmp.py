import sys
import time

import numpy as np
from scipy.io import wavfile

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class GraphAmp(QtWidgets.QMainWindow):

    def __init__(self, wavpath='C:/Users/yetski/Music/Recordings/Recording.wav', rawpath='C:/Users/yetski/Music/Recordings/Raw.txt'):

        super(GraphAmp, self).__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        self.static_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        layout.addWidget(self.static_canvas)
        self.addToolBar(NavigationToolbar(self.static_canvas, self))
        self._static_ax = self.static_canvas.figure.subplots()
        self.wavpath = wavpath
        self.rawpath =rawpath

        self.samplerate = 0
        self.data = []

    def show_plot(self):
        self.samplerate, self.data = wavfile.read(self.wavpath)
        d = open(self.rawpath, 'r').read()
        lines = d.split('\n')
        lines.pop()
        print("test", list(self.data))
        print("test2", lines)
        t = [i for i in range(len(self.data))]
        self._static_ax.plot(t, [int(line) for line in lines], "-")
        self.show()

    def hide_plot(self):
        self.hide()

    def updtate(self,newpath,newraw):
        self.wavpath = newpath
        self.rawpath = newraw
        self.show_plot()

if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = GraphAmp()
    app.show()
    qapp.exec_()
