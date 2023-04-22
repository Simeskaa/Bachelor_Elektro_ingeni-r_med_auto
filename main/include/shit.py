import sys
from PySide6.QtCore import Qt, QTimer, QThreadPool, QRunnable
from PySide6.QtGui import QPainter, QPixmap, QColor, QFont, QBrush
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QDial, QPushButton
import threading
import time
import logging
from direction_and_distance_estimation import angle_cord_estimation


class MainWindow(QMainWindow):
    def __init__(self, range:float = 2000., delay:int = 5):
        super().__init__()
        self.label = QLabel()
        self.canvas = QPixmap(700, 700)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.setFixedSize(700, 700)
        self.radar()

        self.x_square = []
        self.y_square = []
        self.timer_square = []
        self.red_square = []
        self.blue_square = []
        self.counter_square = 0
        self.counted_square = 0

        self.x_circle = []
        self.y_circle = []
        self.timer_circle = []
        self.red_circle = []
        self.blue_circle = []
        self.counter_circle = 0
        self.counted_circle = 0
        self.range = range
        self.delay = delay
        self.test = 0


        self.threadpool = QThreadPool()

        # self.timer = QTimer()
        # self.timer.setInterval(5000)
        # #self.timer.setSingleShot(True)
        # self.timer.timeout.connect(self.removing_from_GUI)
        # self.timer.start()


        #self.timer = QTimer()  # set up your QTimer


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
        self.update()


    def make_square(self, x, y, color_index:int):
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red_square[color_index], 0, self.blue_square[color_index]))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)
        self.update()

    def make_circle(self, x, y, color_index:int):
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red_circle[color_index], 0, self.blue_circle[color_index]))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)
        self.update()


    def update_GUI(self, x:float, y:float, hz:int, angle_overrule:bool):
        if not angle_overrule:
            x_adjusted_square , y_adjusted_square= self.coordinate_center(x=x, y=y)
            self.x_square.append(x_adjusted_square)
            self.y_square.append(y_adjusted_square)
            self.counter_square += 1
            if hz == 260:
                self.red_square.append(0)
                self.blue_square.append(255)
            elif hz == 440:
                self.red_square.append(255)
                self.blue_square.append(0)

        elif angle_overrule:
            x_adjusted_circle, y_adjusted_circle = self.coordinate_center(x=x, y=y)
            self.x_circle.append(x_adjusted_circle)
            self.y_circle.append(y_adjusted_circle)
            self.counter_circle += 1
            if hz == 260:
                self.red_circle.append(0)
                self.blue_circle.append(255)
            elif hz == 440:
                self.red_circle.append(255)
                self.blue_circle.append(0)

        #self.item_placement_on_GUI()
        #pool = QThreadPool.globalInstance()
        #pool.start(QTimer.singleShot(1000, self.removing_from_GUI))
        # self.timer.setInterval(5000)
        # self.timer.timeout.connect(self.removing_from_GUI())  # connect it to your update function
        # self.timer.start()
        #QTimer.singleShot(5, self.removing_from_GUI)
        if self.test == 0:
            self.timer = QTimer()
            self.timer.setInterval(5000)
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.removing_from_GUI)
            self.timer.start()
        logging.info("kjørt gjennom singelshot greiå")





    def item_placement_on_GUI(self):
        if self.counter_square > self.counted_square:
            self.make_square(self.x_square[self.counter_square - 1], self.y_square[self.counter_square - 1], color_index=(self.counter_square - 1))
            self.counted_square += 1

        elif self.counter_circle > self.counted_circle:
            self.make_circle(self.x_circle[self.counter_circle - 1], self.y_circle[self.counter_circle - 1], color_index=(self.counter_circle - 1))
            self.counted_circle += 1

    def removing_from_GUI(self):
        logging.info("look at me, I am mr. REMOVING")
        if self.counter_square > 0:
            self.radar()
            self.x_square.pop(0)
            self.y_square.pop(0)
            self.red_square.pop(0)
            self.blue_square.pop(0)
            self.counter_square -= 1
            self.counted_square -= 1
            #self.square = True

            for i in range(len(self.x_square)):
                # logging.info("Drive_func is about to add remaining boxes")
                self.make_square(self.x_square[i], self.y_square[i], color_index=i)
            #logging.info("removing box")

            for i in range(len(self.x_circle)):
                # logging.info("Drive_func is about to add remaining boxes")
                self.make_circle(self.x_circle[i], self.y_circle[i], color_index=i)
            #logging.info("removed box")

        if self.counter_circle > 0:
            self.radar()
            self.x_circle.pop(0)
            self.y_circle.pop(0)
            self.red_circle.pop(0)
            self.blue_circle.pop(0)
            self.counter_circle -= 1
            self.counted_circle -= 1

            #logging.info("removing circle")

            for i in range(len(self.x_square)):
                self.make_square(self.x_square[i], self.y_square[i], color_index=i)

            for i in range(len(self.x_circle)):
                self.make_circle(self.x_circle[i], self.y_circle[i], color_index=i)
            #logging.info("removed circle")



    def coordinate_center(self, x: float, y: float):  # lag et system hvis x/2000 e øve 1
        center_cord_x = (315. * x / self.range) + 340.
        center_cord_y = -(315. * y / self.range) + 340.
        return center_cord_x, center_cord_y


def test():
    while True:
        time.sleep(3)
        logging.info("Thread test is about to update 1")
        boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = boat.timestamp_2_cord(simulation('45'))
        window.update_GUI(x= boat_coords_x, y=boat_coords_y, hz= 440, angle_overrule= angle_overrule)
        #logging.info("Thread test is updated 1")
        time.sleep(3)
        #logging.info("Thread test is about to update 2")
        window.update_GUI(x=50, y=50, hz= 260, angle_overrule= False)
        time.sleep(2)
        window.update_GUI(x=1000, y=1000, hz= 440, angle_overrule= True)
        #logging.info("Thread test is updated 2")
        time.sleep(3)
        #logging.info("Thread test is about to update 3")
        window.update_GUI(x=-1500, y=1500, hz= 260, angle_overrule= False)
        #logging.info("Thread test is updated 3")

def simulation(boat_placment):
    tdoa_78 = [0, 0.019, 0.029, 0.048]
    tdoa_45 = [0.0, 0.0, 0.03498542274, 0.03498542274]
    tdoa_34 = [0., (1.37 + 0.92) / 343, (1.37 + 0.92 + 9.506) / 343, (1.37 + 0.92 + 9.506 + 1.438 + 0.809) / 343]

    if boat_placment == '78':
        # static simulate time delay of arrive
        # -------------------------------------------------
        t1 = tdoa_78[0]
        t2 = tdoa_78[1]
        t3 = tdoa_78[2]
        t4 = tdoa_78[3]
        mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

    if boat_placment == '45':
        t1 = tdoa_45[0]
        t2 = tdoa_45[1]
        t3 = tdoa_45[2]
        t4 = tdoa_45[3]
        mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

    if boat_placment == '34':
        t1 = tdoa_34[0]
        t2 = tdoa_34[1]
        t3 = tdoa_34[2]
        t4 = tdoa_34[3]
        mic = {'m1': t4, 'm2': t3, 'm3': t2, 'm4': t1}

    tdoa = [mic['m1'], mic['m3'], mic['m2'], mic['m4']]

    return tdoa



app = QApplication(sys.argv)
window = MainWindow()
boat = angle_cord_estimation(dist_short_mic=12, spd_sound=343, max_distance=2000)

#window.show()
#x1 = threading.Thread(target=window.upd, args=())
format = "%(asctime)s: %(message)s"

logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


x2 = threading.Thread(target=test)

x2.start()


window.show()
app.exec()

#https://coderslegacy.com/python/pyqt5-qtimer/


