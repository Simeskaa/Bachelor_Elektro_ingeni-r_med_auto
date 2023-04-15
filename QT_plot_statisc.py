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
      #self.make_line()
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

   def make_line(self, start_cord : dict, end_cord : dict):
      #QLine(350,450)
      list_line = {}
      for i in range(6):
         name = f'l_{i+1}'
         p1 = QPointF(start_cord[f'x_{i+1}'], start_cord[f'y_{i+1}'])
         p2 = QPointF(end_cord[f'x_{i+1}'], end_cord[f'y_{i+1}'])
         list_line[name] = QLineF(p1, p2)

      par_1 = list_line['l_1'].intersects(list_line['l_4'])
      par_2 = list_line['l_3'].intersects(list_line['l_6'])
      par_3 = list_line['l_5'].intersects(list_line['l_2'])

      final_cord = {'par 1': par_1, 'par 2': par_2, 'par 3': par_3}

      #par_11 = list_line['l_1'].intersects(list_line['l_4'])
      #par_12 = list_line['l_1'].intersects(list_line['l_6'])
      #par_13 = list_line['l_2'].intersects(list_line['l_3'])
      #par_14 = list_line['l_2'].intersects(list_line['l_5'])

      #final_cord = { 'par 1': par_11, 'par 2': par_12, 'par 3':par_13, 'par 4': par_14}

      par_12 = list_line['l_1'].intersects(list_line['l_2'])
      par_14 = list_line['l_1'].intersects(list_line['l_4'])
      par_16 = list_line['l_1'].intersects(list_line['l_6'])
      par_52 = list_line['l_5'].intersects(list_line['l_2'])
      par_54 = list_line['l_5'].intersects(list_line['l_4'])
      par_32 = list_line['l_3'].intersects(list_line['l_2'])
      par_36 = list_line['l_3'].intersects(list_line['l_6'])
      par_26 = list_line['l_2'].intersects(list_line['l_6'])
      par_46 = list_line['l_4'].intersects(list_line['l_6'])

      intersection_list = [par_12, par_14, par_16, par_52, par_54, par_32, par_36, par_26, par_46]
      #print(par_12[0]==QLineF.BoundedIntersection)
      #print(intersection_list[1][0])
      bound_inter_list = []
      for i in range(len(intersection_list)):
         if intersection_list[i][0] == QLineF.BoundedIntersection:
            bound_inter_list.append(intersection_list[i][1])
      #print(bound_inter_list[0].x())
      x = 0
      y = 0
      if len(bound_inter_list) > 0:
         for i in range(len(bound_inter_list)):
            x = bound_inter_list[i].x() + x
            y = bound_inter_list[i].y() + y
         x = x/len(bound_inter_list)
         y = y/len(bound_inter_list)
      else:
         print('LAG ET SYSTEM DER VINKEL BLIR PASSA UT ISTEDE SÅ GUI-EN FÅR NÅE DATA!!!!!!!!')

      final_cord = {'par 12': par_12, 'par 14': par_14, 'par 16': par_16, 'par 52': par_52, 'par 54': par_54,
                    'par 32': par_32, 'par 36': par_36, 'par 26': par_26, 'par 46': par_46,}
      return x,y



def cordinate(x, y):  # bære navn trengs
   x_new = x + 340
   y_new = -y + 340
   return x_new, y_new

def cordinate_list_version(list_cord: dict):  # bære navn trengs
   center_cord = {}
   for i in range(6):
      name_x = f'x_{i+1}'
      name_y = f'y_{i+1}'
      center_cord[name_x] = list_cord[name_x] + 340
      center_cord[name_y] = -list_cord[name_y] + 340
      #print(center_cord)

   return center_cord

def polar_to_cartesian(r, vinkel):
   #vinkel += np.pi
   x = r * np.cos(vinkel)
   y = r * np.sin(vinkel)
   return x,y

def polar_to_cartesian_list_version(r, vinkel:dict):
   #vinkel += np.pi
   list_cartesian_cord = {}
   for i in range( 6):
      x_name = f'x_{i+1}'
      y_name = f'y_{i+1}'
      list_cartesian_cord[x_name] = r * np.cos(vinkel[f'angle {i+1}'])
      list_cartesian_cord[y_name] = r * np.sin(vinkel[f'angle {i+1}'])


   return list_cartesian_cord

def main():
   app = QApplication(sys.argv)
   ex = Example()
   x1,y1 = polar_to_cartesian(200, np.pi)
   x1, y1 = cordinate(x1, y1)
   #ex.testUI(x1, y1)
   x2, y2 = polar_to_cartesian(200, np.pi / 2)
   x2, y2 = cordinate(x2, y2)
   #ex.testUI(x2, y2)
   x3, y3 = polar_to_cartesian(200, np.pi / 3)
   x3, y3 = cordinate(x3, y3)
   #ex.testUI(x3, y3)
   x3, y3 = polar_to_cartesian(200, np.pi / 4)
   x3, y3 = cordinate(x3, y3)
   ex.testUI(350, 350)
   #print(f'x er {x}, y er {y}')

   #print(f'x er {x}, y er {y}')
   #ex.make_line()
   ex.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()

