import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import threading

class Example(QWidget):
   def __init__(self):
       super(Example, self).__init__()
       self.initUI()
       self.updatesEnabled()



   def initUI(self):
      self.setGeometry(100,100, 700,700)  #(plassering x, plassering y, størrelse x, størrelse y) (x og y kan væra feil)
      self.setWindowTitle('Draw Demo')

   def testUI(self,x,y):
       self.UiComponents(x, y)
       #self.repaint()




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

def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.testUI(230,402)
    ex.show()
    sys.exit(app.exec())

def GUI(app, ex):
    while True:
        ex.show()
        #ex.exec()
        #app.exec()
        sys.exit(app.exec())

def componenet(ex):
    n = 0
    print('fokk')
    while n < 1000001:
        if n == 1000000:
            ex.testUI(380, 222)
            #ex.update()
            print(n)
        n += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    #x1 = threading.Thread(target=GUI, args=(app,ex,))
    #x1.start()
    x2 = threading.Thread(target=componenet, args=(ex,))
    x2.start()
    ex.show()
    sys.exit(app.exec())
