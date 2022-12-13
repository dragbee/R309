from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Client import Client
import socket
import sys

"""
class MainWindow(QMainWindow):

   def __init__(self):
      super().__init__()

      widget = QWidget()
      self.setCentralWidget(widget)
      grid = QGridLayout()
      widget.setLayout(grid)

      self.__lab = QLabel("Coucou")

      self.__lab2 = QLabel("Connexion")
      self.__conn = QPushButton("Se connecter")
      self.__text = QLabel("")

      self.__os = QPushButton("OS")
      self.__ram = QPushButton("RAM")
      self.__cpu = QPushButton("CPU")
      self.__ip = QPushButton("IP")
      self.__name = QPushButton("NAME")
      self.__text2 = QLabel("")

      self.__csv = QLabel("csv")

      grid.addWidget(self.__lab)
      grid.addWidget(self.__lab2)
      grid.addWidget(self.__conn)
      grid.addWidget(self.__text)
      grid.addWidget(self.__os)
      grid.addWidget(self.__ram)
      grid.addWidget(self.__cpu)
      grid.addWidget(self.__ip)
      grid.addWidget(self.__name)
      grid.addWidget(self.__text2)
      grid.addWidget(self.__csv)
"""

class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)
        self.host = "127.0.0.1"
        self.port = 8111
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        self.connexion = Client("127.0.0.1", 8111)

        self.connip = QLabel("IP")
        self.ip = QLineEdit()
        self.connport = QLabel("PORT")
        self.port = QLineEdit()
        self.conn = QPushButton("Connexion")
        self.connect = QLabel("Déconnecté")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Add message")
        self.text = QLineEdit()
        self.btnPress2 = QPushButton("Clear")

        layout = QGridLayout()
        layout.addWidget(self.connip, 0, 0)
        layout.addWidget(self.ip, 0, 1)
        layout.addWidget(self.connport, 0, 2)
        layout.addWidget(self.port, 0, 3)
        layout.addWidget(self.conn, 0, 4)
        layout.addWidget(self.connect, 1, 0)
        layout.addWidget(self.textEdit, 2, 0, 1, 4)
        layout.addWidget(self.text, 3, 0, 1, 4)
        layout.addWidget(self.btnPress1, 4, 0)
        layout.addWidget(self.btnPress2, 4, 1)

        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.conn.clicked.connect(self.client_connect)

    def btnPress1_Clicked(self):
        x = self.text.text()
        x = str(x)
        self.sock.send(x.encode())
        self.textEdit.append(x)
        self.text.clear()

    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("")

    def msgserv(self, conn):
        data = ""
        while data != "kill":
            data = conn.recv(1024).decode()
            conn.send(data.encode())
            self.textEdit.append(data)

    def client_connect(self):
        host=str(self.ip.text())
        port=int(self.port.text())
        self.connexion = Client.connect(host, port)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())