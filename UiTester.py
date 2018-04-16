import sys
from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseClass = uic.loadUiType('APES.ui')
NewSoundUI, NewSoundBase = uic.loadUiType('NewSound.ui')

class Main(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.record)

    def record(self):
        self.child_window = NewRecording(self)
        self.child_window.show()


class NewRecording(NewSoundUI,NewSoundBase):
    def __init__(self,parent=None):
        NewSoundUI.__init__(self,parent)
        self.setupUI(self)

if __name__ == "__main__":
    app=QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    another = NewRecording()
    another.show()
    sys.exit(app.exec_())