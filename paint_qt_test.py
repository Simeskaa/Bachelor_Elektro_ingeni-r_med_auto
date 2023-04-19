import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import threading
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
        #self.updatesEnabled()
        #self.show()

    def upd(self):
        time.sleep(10)
        print('satan')
        self.repaint(self.canvas)
    def draw_something(self):
        painter = QPainter(self.canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()
        self.label.setPixmap(self.canvas)
        print('faen')

    def draw_something_new(self, x, y):
        time.sleep(5)
        print('test')
        painter = QPainter(self.canvas)
        painter.drawLine(10, 10, x, y)
        painter.end()
        self.label.setPixmap(self.canvas)



app = QApplication(sys.argv)
window = MainWindow()

#window.show()
x1 = threading.Thread(target=window.upd, args=())
x2 = threading.Thread(target=window.draw_something_new, args=(100,50), daemon=True)
x1.start()
x2.start()
window.show()
app.exec()

