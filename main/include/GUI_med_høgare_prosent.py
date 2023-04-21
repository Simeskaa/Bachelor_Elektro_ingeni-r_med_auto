import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap, QColor, QFont, QBrush
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import threading
import time
import logging

class MainWindow(QMainWindow):
    def __init__(self, range:float = 2000., delay: int = 5):
        super().__init__()
        self.label = QLabel()
        self.canvas = QPixmap(700, 700)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.radar()

        self.x = []
        self.y = []
        self.timer = []
        self.red = []
        self.blue = []
        self.counter = 0
        self.counted = 0
        self.range = range
        self.delay = delay
        self.lock = threading.Lock()

    def radar(self):
        self.canvas.fill(Qt.GlobalColor.white)
        painter = QPainter(self.canvas)
        painter.setPen(QColor(Qt.red))
        painter.setPen(QColor(Qt.red))
        painter.setFont(QFont('Arial', 20))
        painter.drawText(348, 35, "0")  # x, y
        painter.drawText(660, 350, "90")
        painter.drawText(325, 680, "180")
        painter.drawText(1, 350, "270")
        painter.setPen(QColor(Qt.black))
        painter.drawEllipse(350, 350, 2, 2)
        painter.drawEllipse(200, 200, 300, 300)
        painter.drawEllipse(50, 50, 600, 600)
        painter.end()
        self.label.setPixmap(self.canvas)

    def make_box(self, x, y, color_index:int):
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red[color_index],0,self.blue[color_index]))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)

    def make_circle(self, x, y, color_index:int):
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red[color_index],0,self.blue[color_index]))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)

    def coordinate_center(self, x: float, y: float):  # lag et system hvis x/2000 e øve 1
        center_cord_x = (315. * x / self.range) + 340.
        center_cord_y = -(315. * y / self.range) + 340.
        return center_cord_x, center_cord_y

    def update_GUI(self, x:float, y:float, hz:int):
            with self.lock:
                cord_x, cord_y = self.coordinate_center(x,y)
                self.x.append(cord_x)
                self.y.append(cord_y)
                self.counter += 1
                self.timer.append(time.perf_counter()+ self.delay)
                if hz == 260:
                    self.red.append(0)
                    self.blue.append(255)
                elif hz == 440:
                    self.red.append(255)
                    self.blue.append(0)

    def item_placement_on_GUI(self):
        while True:
            with self.lock:
                if self.counter > self.counted:
                    self.make_circle(self.x[self.counter - 1], self.y[self.counter - 1], color_index=(self.counter-1))
                    self.counted += 1



                elif self.counter > 0:
                    if self.timer[0] < time.perf_counter():
                        self.x.pop(0)
                        self.y.pop(0)
                        self.timer.pop(0)
                        self.red.pop(0)
                        self.blue.pop(0)
                        self.counter -= 1
                        self.counted -= 1
                        self.radar()
                        for i in range(len(self.x)):
                            self.make_box(self.x[i], self.y[i], color_index= i)



def test():
    time.sleep(3)
    window.update_GUI(300, 250, hz= 440)
    time.sleep(3)
    window.update_GUI(200, 50, hz= 260)
    time.sleep(0.1)
    window.update_GUI(50, 50, hz= 440)
    time.sleep(3)
    window.update_GUI(50, 300, hz= 260)





app = QApplication(sys.argv)
window = MainWindow()

x = threading.Thread(target=window.item_placement_on_GUI)
x2 = threading.Thread(target=test)
x.start()
x2.start()

window.show()
app.exec()