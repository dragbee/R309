import sys
from GI1 import MainWindow
from GI2 import MainWindow2
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    app.exec()