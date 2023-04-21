import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import threading
import time


class WorkerThread(QObject):
    signalExample = Signal(int)

    def __init__(self):
        super().__init__()

    @Slot()
    def run(self):
        while True:
            HOST = '192.168.1.43'  # The server's hostname or IP address, NodeMCU IP Address
            PORT = 80  # The port used by the server, PORT NUMBER in ARDUINO CODE
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(b'Hello, world')
                data = s.recv(1024)
            print('Received duration value', repr(data))
            self.signalExample.emit(data)
            time.sleep(1)


class WorkerLabel(QLabel):
    def __init__(self, parent):
        super().__init__()

    @Slot(int)
    def slot(self, i):
        self.setText(str(i))


class UserInterface():
    def __init__(self, parent):
        super().__init__()
        self.paintEvent()

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


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UserInterface(self)
        self.setCentralWidget(self.ui)

        self.worker = WorkerThread()
        self.workerThread = QThread()  # Move the Worker object to the Thread object
        self.workerThread.started.connect(self.worker.run)  # Init worker run() at startup
        self.worker.moveToThread(self.workerThread)
        self.worker.signalExample.connect(self.signalExample)
        self.workerThread.start()

        self.show()

    def signalExample(self, number):
        print(number)


if __name__ == '__main__':
    app = QApplication([])
    gui = Main()
    sys.exit(app.exec_())