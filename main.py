import math
import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QListWidget, QLineEdit, QPushButton, QRadioButton
from PyQt5.QtWidgets import QSpinBox, QLabel, QLCDNumber, QListView, QMainWindow, QApplication


class FildWord(QMainWindow):
    def __init__(self):
        super(FildWord, self).__init__()
        uic.loadUi('project 1.ui', self)

        self.generatorButton.clicked.connect(self.generate)

    def generate(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())
