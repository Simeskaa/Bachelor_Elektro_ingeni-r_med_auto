import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import numpy as np


class Example(QWidget):
   def __init__(self):
      super().__init__()
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
      #self.show()


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
    n = 0
    app = QApplication(sys.argv)
    ex = Example()
    if n == 0:
        x,y = polar_to_cartesian(200, 2*np.pi)
        x, y = cordinate(x,y)
        ex.testUI(x, y)
    if n == 1:
        x,y = polar_to_cartesian(200, np.pi)
        x, y = cordinate(x,y)
        ex.testUI(x, y)
    #ex.show()
    #sys.exit(app.exec())
    ex.exec()
    n += 1
    n %= 2
    print(n)



if __name__ == '__main__':
   main()

