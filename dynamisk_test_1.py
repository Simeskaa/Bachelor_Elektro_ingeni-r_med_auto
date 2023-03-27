import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QDialog, QLayout, QGridLayout,
                               QMessageBox, QGroupBox, QSpinBox, QSlider,
                               QProgressBar, QDial, QDialogButtonBox,
                               QComboBox, QLabel)
from PySide6.QtGui import *


class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        #plassering av sonan
        main_layout = QGridLayout()


        self._main_layout = main_layout
        self.setLayout(self._main_layout)

        self.setWindowTitle("Dynamic Layouts")

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.red))
        qp.setFont(QFont('Arial', 20))
        qp.drawText(348, 35, "0")  # x, y
        # qp.drawText(1000, 5000, "15")
        # qp.drawText(1000, 5000, "30")
        # qp.drawText(1000, 5000, "45")
        # qp.drawText(1000, 5000, "60")
        # qp.drawText(1000, 5000, "75")
        qp.drawText(660, 350, "90")
        # qp.drawText(1000, 5000, "105")
        # qp.drawText(1000, 5000, "120")
        # qp.drawText(1000, 5000, "135")
        # qp.drawText(1000, 5000, "150")
        # qp.drawText(1000, 5000, "165")
        qp.drawText(325, 680, "180")
        # qp.drawText(1000, 5000, "195")
        # qp.drawText(1000, 5000, "210")
        # qp.drawText(1000, 5000, "225")
        # qp.drawText(1000, 5000, "240")
        # qp.drawText(1000, 5000, "255")
        qp.drawText(1, 350, "270")
        # qp.drawText(1000, 5000, "285")
        # qp.drawText(1000, 5000, "300")
        # qp.drawText(1000, 5000, "315")
        # qp.drawText(1000, 5000, "330")
        # qp.drawText(1000, 5000, "345")
        qp.setPen(QColor(Qt.black))
        qp.drawEllipse(350, 350, 2, 2)
        qp.drawEllipse(200, 200, 300, 300)
        qp.drawEllipse(50, 50, 600, 600)

        qp.end()




if __name__ == '__main__':


    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec()