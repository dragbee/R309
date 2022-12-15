from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Client import Client
import socket
import sys
import threading

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
        self.setWindowTitle("︻╦╤─")
        self.resize(500, 470)
        self.connexion = Client("127.0.0.1", 8111)

        self.connip = QLabel("IP")
        self.ip = QLineEdit("127.0.0.1")
        self.connport = QLabel("PORT")
        self.port = QLineEdit("8111")
        self.conn = QPushButton("Connexion")
        self.deconn = QPushButton("Déconnexion")
        self.deconn.setEnabled(False)
        self.connect = QLabel("Déconnecté")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Add message")
        self.btnPress1.setEnabled(False)
        self.texto = QLineEdit('')
        self.btnPress2 = QPushButton("Clear")
        self.btnPress2.setEnabled(False)
        self.win = None
        self.button = QPushButton("Open Window")

        layout = QGridLayout()
        layout.addWidget(self.connip, 0, 0)
        layout.addWidget(self.ip, 0, 1)
        layout.addWidget(self.connport, 0, 2)
        layout.addWidget(self.port, 0, 3)
        layout.addWidget(self.conn, 0, 4)
        layout.addWidget(self.deconn, 0, 5)
        layout.addWidget(self.connect, 1, 0)
        layout.addWidget(self.textEdit, 2, 0, 1, 4)
        layout.addWidget(self.texto, 3, 0, 1, 4)
        layout.addWidget(self.btnPress1, 4, 0)
        layout.addWidget(self.btnPress2, 4, 1)
        layout.addWidget(self.button, 5, 0)


        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.envoie)
        self.btnPress2.clicked.connect(self.clear)
        self.conn.clicked.connect(self.client_connect)
        self.deconn.clicked.connect(self.client_disconnect)
        self.button.clicked.connect(self.open_window)

    def envoie(self):
        msg = self.texto.text()
        msg = str(msg)
        self.socket.send(msg.encode())
        self.textEdit.append(msg)
        self.thread = threading.Thread(target=self.reception, args=[self.socket, ])
        self.thread.start()
        self.texto.clear()

    def reception(self, conn):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = conn.recv(1024).decode()
            self.textEdit.append(msg)
            print(msg)

    def clear(self):
        self.textEdit.setPlainText("")


    def client_connect(self):
        errc = QMessageBox()
        errc.setWindowTitle("ERREUR")
        errc.setText("Adresse ou port non valide, assurez-vous d'avoir la bonne adresse ou le bon port")

        try:
            self.socket = socket.socket()
            ip = str(self.ip.text())
            port = int(self.port.text())
            self.socket.connect((ip, port))
            self.connect.setText("connecté")
            self.conn.setEnabled(False)
            self.btnPress1.setEnabled(True)
            self.btnPress2.setEnabled(True)
            self.deconn.setEnabled(True)
        except:
            errc.exec()



    def client_disconnect(self):
        self.connect.setText("déconnecté")
        self.conn.setEnabled(True)
        self.btnPress1.setEnabled(False)
        self.btnPress2.setEnabled(False)
        self.deconn.setEnabled(False)
        self.textEdit.clear()
        self.socket.close()


    def open_window(self):
        self.win = TextEditDemo()
        self.win.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())