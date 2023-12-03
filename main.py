import sys
import math  # +++
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QPointF
from PyQt5 import QtCore, QtGui, QtWidgets


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 1000, 1000)
        self.btn = QPushButton('click', self)
        self.btn.setGeometry(200, 200, 50, 50)
        self.btn.clicked.connect(self.push)

    def push(self):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)

    def draw_circle(self, qp):
        a = self.getRandomSize()
        qp.setBrush(self.getRandomColor())
        qp.drawEllipse(150, 150, a, a)

    def getRandomSize(self):
        return randint(10, 100)

    def getRandomColor(self):
        return QColor(randint(0, 255), randint(0, 255), randint(0, 255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
