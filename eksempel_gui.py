import sys
import time
# import random
import socket
from PyQt5 import QtWidgets, QtCore


class WorkerThread(QtCore.QObject):
    signalExample = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    @QtCore.pyqtSlot()
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


class WorkerLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__()

    @QtCore.pyqtSlot(int)
    def slot(self, i):
        self.setText(str(i))


class UserInterface(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.label = WorkerLabel(self)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UserInterface(self)
        self.setCentralWidget(self.ui)

        self.worker = WorkerThread()
        self.workerThread = QtCore.QThread()  # Move the Worker object to the Thread object
        self.workerThread.started.connect(self.worker.run)  # Init worker run() at startup
        self.worker.moveToThread(self.workerThread)
        self.worker.signalExample.connect(self.signalExample)
        self.workerThread.start()

        self.show()

    def signalExample(self, number):
        print(number)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    gui = Main()
    sys.exit(app.exec_())