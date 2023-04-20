import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap, QColor, QFont, QBrush
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import threading
import time
import logging

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.canvas = QPixmap(700, 700)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.radar()

        self.x = []
        self.y = []
        self.timer = []
        self.counter = 0
        self.counted = 0
        self.lock = threading.Lock()
        self.red = 0
        self.blue = 0
        #self.box()
        #self.draw_something()
        #self.updatesEnabled()
        #self.UiComponents(50,50,vis= False)
        #self.show()

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

    def make_box(self, x, y):
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red,0,self.blue))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)

    def make_circle(self, x, y):
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red,0,self.blue))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)

    def update_GUI(self, x:float, y:float, hz:int):
            with self.lock:
                self.x.append(x)
                self.y.append(y)
                self.counter += 1
                self.timer.append(time.perf_counter()+5)
                if hz == 260:
                    self.red = 0
                    self.blue = 255
                elif hz == 440:
                    self.red = 255
                    self.blue = 0

    def item_placement_on_GUI(self):
        while True:
            if self.counter > self.counted:
                with self.lock:
                    logging.info("drive_func adding box")
                    self.make_circle(self.x[self.counter - 1], self.y[self.counter - 1])
                    self.counted += 1
                    logging.info("drive_func added box")



            elif self.counter > 0:
                if self.timer[0] < time.perf_counter():
                    with self.lock:
                        logging.info("drive_func is about to remove box")
                        self.x.pop(0)
                        self.y.pop(0)
                        self.timer.pop(0)
                        self.counter -= 1
                        self.counted -= 1
                        logging.info("drive_func have removed box and clean radar")
                        self.radar()
                        logging.info("drive_func have cleaned radar")
                        for i in range(len(self.x)):
                            logging.info("Drive_func is about to add remaining boxes")
                            self.make_box(self.x[i], self.y[i])
                            logging.info("Drive_func have added one of remaining boxes")



def test():
    time.sleep(3)
    logging.info("Thread test is about to update 1")
    window.update_GUI(400, 250, hz= 260)
    logging.info("Thread test is updated 1")
    time.sleep(3)
    logging.info("Thread test is about to update 2")
    window.update_GUI(500, 50, hz= 260)
    logging.info("Thread test is updated 2")
    time.sleep(3)
    logging.info("Thread test is about to update 3")
    window.update_GUI(50, 300, hz= 260)
    logging.info("Thread test is updated 3")





app = QApplication(sys.argv)
window = MainWindow()

#window.show()
#x1 = threading.Thread(target=window.upd, args=())
format = "%(asctime)s: %(message)s"

logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

x = threading.Thread(target=window.item_placement_on_GUI)
x2 = threading.Thread(target=test)
x.start()
x2.start()

window.show()
app.exec()

