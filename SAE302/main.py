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
import sys
from PyQt5.QtWidgets import *
from GUI import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()