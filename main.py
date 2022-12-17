import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

UI_PATH = "UI.ui"


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)
        self.setEvents()

    def setEvents(self):
        self.spawnButton.clicked.connect(self.spawnButtonClicked)

    def spawnButtonClicked(self, event):
        print("clicked")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
