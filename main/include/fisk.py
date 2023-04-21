from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
import sys

def my_function():
    print("Timer fired!")


app = QApplication(sys.argv)
QTimer.singleShot(1000, my_function)
sys.exit(app.exec())