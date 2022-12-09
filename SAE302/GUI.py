from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Client import Client
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

        self.connip = QLabel("IP")
        self.ip = QLineEdit()
        self.connport = QLabel("PORT")
        self.port = QLineEdit()
        self.conn = QPushButton("Connexion")
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Add message")
        self.text = QTextEdit()
        self.btnPress2 = QPushButton("Clear")

        layout = QGridLayout()
        layout.addWidget(self.connip, 0, 0)
        layout.addWidget(self.ip, 0, 1)
        layout.addWidget(self.connport, 0, 2)
        layout.addWidget(self.port, 0, 3)
        layout.addWidget(self.conn, 0, 4)
        layout.addWidget(self.textEdit, 1, 0, 1, 4)
        layout.addWidget(self.text, 2, 0, 1, 4)
        layout.addWidget(self.btnPress1, 3, 0)
        layout.addWidget(self.btnPress2, 3, 1)

        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.conn.clicked.connect(self.client_connect)

    def btnPress1_Clicked(self):
        self.textEdit.append(f"{self.text.toPlainText()}")
        self.text.clear()
#        self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("")
#        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")

    def client_connect(self, host, port):
        self.client = Client.connect
        return (self.client())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
