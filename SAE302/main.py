"""
import platform
""
print(platform.uname())

from Client import server_socket

host = input("hostname : ")
port = input("port : ")
serv = server_socket(host, port)
serv.connect()
rep = serv.send()
if rep == "":
    print("serveur no connecté")
else:
    print(rep)
"""
"""
import sys
from PyQt5.QtWidgets import *
from GUI import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

# Create the main window
main_window = QWidget()

# Create the button
button = QPushButton("Open Window", main_window)


# Create the window
window = QWidget()
window.setWindowTitle("Window")

def open_window():
    window.show()

button.clicked.connect(open_window)
main_window.show()
sys.exit(app.exec_())