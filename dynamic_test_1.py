import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QDialog, QLayout, QGridLayout,
                               QMessageBox, QGroupBox, QSpinBox, QSlider,
                               QProgressBar, QDial, QDialogButtonBox,
                               QComboBox, QLabel, QCheckBox)
from PySide6.QtGui import *
import threading
import time

import numpy as np


class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        #plassering av sonan
        main_layout = QGridLayout()


        self._main_layout = main_layout
        self.setLayout(self._main_layout)
        self.setGeometry(100, 100, 700, 700)
        self.setWindowTitle("Dynamic Layouts")

    def UiComponents(self, x, y):
        # creating the check-box
        checkbox = QCheckBox('', self)

        # setting geometry of check box
        checkbox.setGeometry(x, y, 100, 30)

        # adding background color to indicator
        checkbox.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "background-color : red;"
                               "}")

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.red))
        qp.setFont(QFont('Arial', 20))
        qp.drawText(348, 35, "0")  # x, y
        qp.drawText(660, 350, "90")
        qp.drawText(325, 680, "180")
        qp.drawText(1, 350, "270")
        qp.setPen(QColor(Qt.black))
        qp.drawEllipse(350, 350, 2, 2)
        qp.drawEllipse(200, 200, 300, 300)
        qp.drawEllipse(50, 50, 600, 600)

        qp.end()

def cordinate(x, y):  # bære navn trengs
   x_new = x + 350
   y_new = -y + 350
   return x_new, y_new

def polar_to_cartesian(r, vinkel):
   x = r * np.cos(vinkel)
   y = r * np.sin(vinkel)
   return x,y

def go(dialog):
    x, y = polar_to_cartesian(200, np.pi)
    x, y = cordinate(x, y)
    n = 0
    print('fokk')
    while n < 101:
        if n == 100:
            dialog.UiComponents(x, y)
            print(n)
        n += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    x = threading.Thread(target=go, args=(dialog,))
    x.start()
    #time.sleep(5)
    dialog.exec()

