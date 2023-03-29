"""

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QPainter, QBrush, QPen


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.circle = QtWidgets.QGraphicsEllipseItem()


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.circle)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    def paint(self):
        painter = QPainter(self)
        painter.drawEllipse(40,40,400,400)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    #widget.paint()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
    """

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import numpy as np


class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()
      self.initUI()

   def initUI(self):
      #  self.text = "hello world"
      self.setGeometry(100,100, 700,700)  #(plassering x, plassering y, størrelse x, størrelse y) (x og y kan væra feil)
      self.setWindowTitle('Draw Demo')
      #self.UiComponents()
      #self.show()

   def testUI(self,x,y):
      #  self.text = "hello world"
      self.UiComponents(x,y)
      self.show()


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

def cordinate(x, y):  # bære navn trengs
   x_new = x + 350
   y_new = -y + 350
   return x_new, y_new

def polar_to_cartesian(r, vinkel):
   x = r * np.cos(vinkel)
   y = r * np.sin(vinkel)
   return x,y

def main():
   app = QApplication(sys.argv)
   ex = Example()
   x,y = polar_to_cartesian(300, np.pi)
   print(f'x er {x}, y er {y}')
   x, y = cordinate(x,y)
   print(f'x er {x}, y er {y}')
   ex.testUI(x, y)

   sys.exit(app.exec())

if __name__ == '__main__':
   main()

