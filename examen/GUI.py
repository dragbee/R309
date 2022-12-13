from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from client import Client
import socket

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Un logiciel de tchat")
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.connexion = Client("127.0.0.1", 10000)

        self.labserv = QLabel("Serveur")
        self.textserv = QLineEdit("localhost")
        self.labport = QLabel("Port")
        self.textport = QLineEdit("10000")

        self.connexion = QPushButton("Connexion")

        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)

        self.labmess = QLabel("Message :")
        self.textmess = QTextEdit("")
        self.textmess.setEnabled(False)
        self.envoyer = QPushButton("Envoyer")
        self.envoyer.setEnabled(False)

        self.effacer = QPushButton("Effacer")
        self.quitter = QPushButton("Quitter")





        grid.addWidget(self.labserv)
        grid.addWidget(self.textserv, 0, 1)
        grid.addWidget(self.labport, 1, 0)
        grid.addWidget(self.textport, 1, 1)
        grid.addWidget(self.connexion, 2, 0, 1, 2)
        grid.addWidget(self.textEdit, 3, 0, 1, 2)
        grid.addWidget(self.labmess, 4, 0)
        grid.addWidget(self.textmess, 4, 1)
        grid.addWidget(self.envoyer, 5, 0, 1, 2)
        grid.addWidget(self.effacer, 6, 0)
        grid.addWidget(self.quitter, 6, 1)

        self.envoyer.clicked.connect(self._envoyer)
        self.effacer.clicked.connect(self._effacer)
        self.quitter.clicked.connect(self._quitter)
        self.connexion.clicked.connect(self.client_connect)

    def _envoyer(self):
        self.textEdit.append(f"{self.textmess.toPlainText()}")
        self.textmess.clear()

    def _effacer(self):
        self.textEdit.setPlainText("")

    def _quitter(self):
        self.textEdit.setText("deco-server")
        QCoreApplication.exit(0)

    def client_connect(self):
        errc = QMessageBox()
        errc.setWindowTitle("ERREUR")
        errc.setText("Adresse ou port non valide, assurez-vous d'avoir <<localhost, 10000>>")

        host=str(self.textserv.text())
        port=int(self.textport.text())
        self.connexion = Client(host, port)
        try:
            self.connexion.connect()
            self.envoyer.setEnabled(True)
            self.textmess.setEnabled(True)
        except:
            errc.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
