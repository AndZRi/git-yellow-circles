import sys

from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from UI import Ui_MainWindow

CIRCLE_MAX_SIZE = 200
CIRCLE_MIN_SIZE = 50


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.setEvents()

    def setEvents(self):
        self.spawnButton.clicked.connect(self.spawnButtonClicked)

    def spawnButtonClicked(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        if self.do_paint:
            self.spawnRandomCircle(QtGui.QPainter(self))
        self.do_paint = False

    def spawnRandomCircle(self, painter: QtGui.QPainter):
        diameter = randint(CIRCLE_MIN_SIZE, CIRCLE_MAX_SIZE)
        x = randint(0, self.width())
        y = randint(0, self.height())

        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        painter.setBrush(QtGui.QColor(r, g, b))
        painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
