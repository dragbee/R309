from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__lab2 = QLabel()
        self.__lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__ok = QPushButton("Ok")
        self.__quit = QPushButton("Quitter")


        # Ajouter les composants au grid ayout
        self.__ok.clicked.connect(self.__actionOk)
        self.__quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Une première fenêtre")

        grid.addWidget(self.__lab)
        grid.addWidget(self.__text)
        grid.addWidget(self.__ok, 0, 1)
        grid.addWidget(self.__lab2)
        grid.addWidget(self.__quit, 1, 1)

    def __actionOk(self):
        nom = self.__text.text()
        self.__lab2.setText(f"Bonjour {nom} !")

    def __actionQuitter(self):
        QCoreApplication.exit(0)


