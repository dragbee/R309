from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


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
