import sys
from PySide6.QtCore import Qt, QTimer, QThreadPool, QMutex
from PySide6.QtGui import QPainter, QPixmap, QColor, QFont, QBrush
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import threading
import time
import logging
import numpy as np
from memory_profiler import profile


class GUI(QMainWindow):
    def __init__(self, max_dist:float = 100., delay: int = 5):
        super().__init__()
        # making the canvas and plotting the radar
        self.label = QLabel()
        self.canvas = QPixmap(700, 700)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.setFixedSize(700, 700)
        self.radar()

        # making variables for placement of the objects
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

        self.x_rect_circle = []
        self.y_rect_circle = []
        self.timer_rect_circle = []
        self.red_rect_circle = []
        self.blue_rect_circle = []
        self.counter_rect_circle = 0
        self.counted_rect_circle = 0

        self.adding_object = False

        # making timer for removel for objects
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.removing_from_GUI)
        self.timer.start()

        # making variables for max distance and delay to removel of objects
        self.max_dist = max_dist
        self.delay = delay

    #@profile
    def radar(self):
        # painting the radar on the canvas
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
        # making a squire for representation for object
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
        # making a squire for representation for object
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red_circle[color_index], 0, self.blue_circle[color_index]))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(x, y, 10, 10)
        painter.end()
        self.label.setPixmap(self.canvas)
        self.update()

    def make_rect_circle(self, x, y, color_index:int):
        # making a squire for representation for object
        painter = QPainter(self.canvas)
        brush = QBrush()
        brush.setColor(QColor(self.red_rect_circle[color_index], 0, self.blue_rect_circle[color_index]))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRoundedRect(x, y, 10, 10, 2, 2)
        painter.end()
        self.label.setPixmap(self.canvas)
        self.update()

    #@profile
    def update_GUI(self, x:float, y:float, hz:str, angle_overrule:bool):
        self.adding_object = True
        x_adjusted, y_adjusted, out_of_bound = self.coordinate_center(x=x, y=y)
        if not angle_overrule:
            if out_of_bound:
                self.x_rect_circle.append(x_adjusted)
                self.y_rect_circle.append(y_adjusted)
                self.counter_rect_circle += 1
                self.timer_rect_circle.append(time.perf_counter() + self.delay)
                if hz == '260':
                    self.red_rect_circle.append(0)
                    self.blue_rect_circle.append(255)
                elif hz == '440':
                    self.red_rect_circle.append(255)
                    self.blue_rect_circle.append(0)
            else:
                self.x_square.append(x_adjusted)
                self.y_square.append(y_adjusted)
                self.counter_square += 1
                self.timer_square.append(time.perf_counter() + self.delay)
                if hz == '260':
                    self.red_square.append(0)
                    self.blue_square.append(255)
                elif hz == '440':
                    self.red_square.append(255)
                    self.blue_square.append(0)

        elif angle_overrule:
            # updating GUI, if angle overrule, the angle and distance estimation class couldn't find the distance and
            # only the angle
            self.x_circle.append(x_adjusted)
            self.y_circle.append(y_adjusted)
            self.timer_circle.append(time.perf_counter() + self.delay)
            self.counter_circle += 1
            if hz == '260':
                self.red_circle.append(0)
                self.blue_circle.append(255)
            elif hz == '440':
                self.red_circle.append(255)
                self.blue_circle.append(0)
        self.item_placement_on_GUI()

    #@profile
    def item_placement_on_GUI(self):
        # placing the object on the radar
        if self.counter_square > self.counted_square:
            self.make_square(self.x_square[self.counter_square - 1], self.y_square[self.counter_square - 1], color_index=(self.counter_square - 1))
            self.counted_square += 1

        elif self.counter_circle > self.counted_circle:
            self.make_circle(self.x_circle[self.counter_circle - 1], self.y_circle[self.counter_circle - 1], color_index=(self.counter_circle - 1))
            self.counted_circle += 1

        elif self.counter_rect_circle > self.counted_rect_circle:
            self.make_rect_circle(self.x_rect_circle[self.counter_rect_circle - 1], self.y_rect_circle[self.counter_rect_circle - 1], color_index=(self.counter_rect_circle - 1))
            self.counted_rect_circle += 1
        self.adding_object = False

    #@profile
    def removing_from_GUI(self):
        # removing the object from the radar
        if not self.adding_object:
            if self.counter_square > 0:
                if self.timer_square[0] < time.perf_counter():
                    # deleting the oldest object in the different lists
                    self.radar()
                    self.x_square.pop(0)
                    self.y_square.pop(0)
                    self.red_square.pop(0)
                    self.blue_square.pop(0)
                    self.timer_square.pop(0)
                    self.counter_square -= 1
                    self.counted_square -= 1

                    # adding the remaking objects on the radar again
                    for i in range(len(self.x_square)):
                        self.make_square(self.x_square[i], self.y_square[i], color_index=i)

                    if self.counter_circle > 0:
                        for i in range(len(self.x_circle)):
                            self.make_circle(self.x_circle[i], self.y_circle[i], color_index=i)

                    if self.counter_rect_circle > 0:
                        for i in range(len(self.x_rect_circle)):
                            self.make_rect_circle(self.x_rect_circle[i], self.y_rect_circle[i], color_index=i)

            if self.counter_circle > 0:
                if self.timer_circle[0] < time.perf_counter():
                    # deleting the oldest object in the different lists
                    self.radar()
                    self.x_circle.pop(0)
                    self.y_circle.pop(0)
                    self.red_circle.pop(0)
                    self.blue_circle.pop(0)
                    self.timer_circle.pop(0)
                    self.counter_circle -= 1
                    self.counted_circle -= 1

                    # adding the remaking objects on the radar again
                    if self.counter_square > 0:
                        for i in range(len(self.x_square)):
                            self.make_square(self.x_square[i], self.y_square[i], color_index=i)

                    for i in range(len(self.x_circle)):
                        self.make_circle(self.x_circle[i], self.y_circle[i], color_index=i)

                    if self.counter_rect_circle > 0:
                        for i in range(len(self.x_rect_circle)):
                            self.make_rect_circle(self.x_rect_circle[i], self.y_rect_circle[i], color_index=i)

            if self.counter_rect_circle > 0:
                if self.timer_rect_circle[0] < time.perf_counter():
                    # deleting the oldest object in the different lists
                    self.radar()
                    self.x_rect_circle.pop(0)
                    self.y_rect_circle.pop(0)
                    self.red_rect_circle.pop(0)
                    self.blue_rect_circle.pop(0)
                    self.timer_rect_circle.pop(0)
                    self.counter_rect_circle -= 1
                    self.counted_rect_circle -= 1

                    # adding the remaking objects on the radar again
                    if self.counter_square > 0:
                        for i in range(len(self.x_square)):
                            self.make_square(self.x_square[i], self.y_square[i], color_index=i)

                    if self.counter_circle > 0:
                        for i in range(len(self.x_circle)):
                            self.make_circle(self.x_circle[i], self.y_circle[i], color_index=i)

                    for i in range(len(self.x_rect_circle)):
                        self.make_rect_circle(self.x_rect_circle[i], self.y_rect_circle[i], color_index=i)


    def coordinate_center(self, x: float, y: float):
        # centring the coordinates so it fit the GUI
        x_scalar = x / self.max_dist
        y_scalar = y / self.max_dist
        out_of_bound = False

        if x_scalar > 1.:
            x_scalar = 1.
            out_of_bound = True
        elif x_scalar < -1.:
            x_scalar = -1.
            out_of_bound = True
        if y_scalar > 1.:
            y_scalar = 1.
            out_of_bound = True
        elif y_scalar < -1.:
            y_scalar = -1.
            out_of_bound = True

        center_cord_x = (265. * x_scalar) + 350.
        center_cord_y = -(265. * y_scalar) + 350.

        return center_cord_x, center_cord_y, out_of_bound


def test():
    # simulating inputs from direction and angle class
    while True:
        #time.sleep(3)
        #boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = boat.timestamp_2_cord(simulation('45'))
        logging.info("starting")
        window.update_GUI(x= 5, y=5, hz= '440', angle_overrule= False)
        time.sleep(1)
        window.update_GUI(x=2500, y=50, hz= '260', angle_overrule= False)
        time.sleep(1)
        window.update_GUI(x=15, y=5, hz= '440', angle_overrule= True)
        time.sleep(1)
        window.update_GUI(x=-1500, y=1500, hz= '260', angle_overrule= False)
        time.sleep(1)
        window.update_GUI(x=-2500, y=1500, hz='260', angle_overrule=False)
        time.sleep(1)
        window.update_GUI(x=-2500, y=-2500, hz='260', angle_overrule=False)
        time.sleep(1)


def simulation(boat_placment):
    # simulating timestamps for the simulation
    tdoa_78 = [0, 0.029, 0.019, 0.048]
    tdoa_45 = [0.0, 0.0, 0.03498542274, 0.03498542274]
    tdoa_34 = [0., (1.37 + 0.92) / 343, (1.37 + 0.92 + 9.506) / 343, (1.37 + 0.92 + 9.506 + 1.438 + 0.809) / 343]

    if boat_placment == '78':
        # static simulate time delay of arrive
        # -------------------------------------------------
        t1 = tdoa_78[0]
        t2 = tdoa_78[1]
        t3 = tdoa_78[2]
        t4 = tdoa_78[3]
        mic = {'m1': t1, 'm2': t3, 'm3': t2, 'm4': t4}

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

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = GUI(max_dist=100, delay=10000)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    #boat = angle_cord_estimation(dist_short_mic=12, spd_sound=343, max_distance=2000)
    x2 = threading.Thread(target=test)
    x2.start()
    window.show()
    app.exec()
