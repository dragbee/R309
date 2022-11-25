from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow2(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__lab = QLabel("Température")
        self.__text = QLineEdit("")
        self.__labc = QLabel("°C")

        self.__conv = QPushButton("Convertir")
        self.__combo = QComboBox()
        self.__combo.addItems(["°C -> K", "K -> °C"])

        self.__lab2 = QLabel("Conversion")
        self.__text2 = QLabel("")
        self.__labk = QLabel("K")

        self.__buttonhelp = QPushButton("?")

        self.__combo.activated.connect(self.__combobox)
        self.__conv.clicked.connect(self.__conversion)
        self.__buttonhelp.clicked.connect(self.__help)


        grid.addWidget(self.__lab)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(self.__labc, 0, 2)
        grid.addWidget(self.__conv, 1, 1)
        grid.addWidget(self.__combo, 1, 2)
        grid.addWidget(self.__lab2, 2, 0)
        grid.addWidget(self.__text2, 2, 1)
        grid.addWidget(self.__labk, 2, 2)
        grid.addWidget(self.__buttonhelp, 3, 2)

    def __combobox(self):
        if self.__combo.currentText() == "°C -> K":
            self.__labc.setText("°C")
            self.__labk.setText("K")
        elif self.__combo.currentText() == "K -> °C":
            self.__labc.setText("K")
            self.__labk.setText("°C")

    def __conversion(self):
        err = QMessageBox()
        err.setWindowTitle("ERREUR")
        err.setText("Température non valide")

        errc = QMessageBox()
        errc.setWindowTitle("ERREUR")
        errc.setText("Température en Kelvin en-dessous de 0")

        c = float(self.__text.text())
        try:
            c
        except:
            err.exec()
        else:
            if self.__combo.currentText() == "°C -> K":
                if c < -273.15:
                    errc.exec()
                else:
                    self.__text2.setText(f"{c + round(273.15, 2)}")
            elif self.__combo.currentText() == "K -> °C":
                if c < 0:
                    errc.exec()
                else:
                    self.__text2.setText(f"{c - round(273.15, 2)}")

    def __help(self):
        dlg = QMessageBox()
        dlg.setIcon()
        dlg.setWindowTitle("AIDE")
        dlg.setText("Permet de convertir un nombre soit de Kelvin vers Celcius, soit de Celsius vers Kelvin.")
        dlg.exec()
