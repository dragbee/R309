
import threading
import socket
import os


# ------------------------------------------------------
class threadReception(threading.Thread):  # thread de reception pour chaque mySocket existante

    def __init__(self, aself):
        threading.Thread.__init__(self)
        self.aself = aself  # héritage du self
        self.isALive = True

    def run(self):
        while self.isALive:
            message = self.aself.mySocket.recv(1024).decode('utf8')  # on recoit les infos de cet communication
            if not message:
                pass

            else:
                print(message)

        mySocket.close()


class client():  # classe de base, pour mika

    def __init__(self, ip, port=22000):  # initialisation de l'ip, port
        self.IP = ip
        self.PORT = port
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # création du socket

    def start(self):  # methode a lancer pour tout initialiser
        try:
            self.mySocket.connect((self.IP, self.PORT))  # connexion
            b = threadReception(self)
            b.start()
            return True
        except Exception as e:
            print(e)
            return False

    def stop(self):  # lorsqu'on étein la table, on etein le serveur
        self.clientALive = False
        self.mySocket.close()

    def send(self, message):  # méthode pour envoyer un message à l'adresse choisie
        try:
            self.mySocket.send(message.encode('utf8'))  # envoi du message
        except Exception as e:
            print(e)
            print('appareil faux/ pb de connexion')


while 1:
    a = client('localhost', 8000)
    a.start()
    msg = input('> ')
    a.send(msg)