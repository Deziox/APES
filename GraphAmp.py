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

        static_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self))

        # dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        # layout.addWidget(dynamic_canvas)
        # self.addToolBar(QtCore.Qt.BottomToolBarArea,
        #                 NavigationToolbar(dynamic_canvas, self))

        samplerate, data = wavfile.read(wavpath)
        d = open(rawpath, 'r').read()
        lines = d.split('\n')
        lines.pop()
        print("test", list(data))
        print("test2", lines)
        # times = np.arange(len(data)) / float(samplerate)

        self._static_ax = static_canvas.figure.subplots()
        t = [i for i in range(len(data))]
        self._static_ax.plot(t, [int(line) for line in lines], "-")
'''
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])
        self._timer.start()
        

    def _update_canvas(self):
        self._dynamic_ax.clear()
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._dynamic_ax.plot(t, np.sin(t + time.time()))
        self._dynamic_ax.figure.canvas.draw()
'''

if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = GraphAmp()
    app.show()
    qapp.exec_()
