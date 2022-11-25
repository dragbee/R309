
import threading
import socket
import os
import time


class threadReception(threading.Thread):  # thread de reception pour chaque connexion existante

    def __init__(self, envoi, add, conn):
        threading.Thread.__init__(self)
        self.addresse = add  # adresse pour recuperer la connexion / supprimer
        self.connexion = conn  # csocket de communication (unique a chaque connexion)
        self.envoi = envoi  # héritage du self
        self.isALive = True

    def run(self):
        while self.isALive:
            message = self.connexion.recv(1024).decode('utf8')  # on recoit les infos de cet communication
            if not message:
                pass

            else:
                print(message)
        self.connexion.close()  # on ferme le socket
        del self.envoi.connectedList[self.addresse]  # on suprime la connexion du dictionnaire


class serveur(threading.Thread):  # classe de base, pour mika

    def __init__(self, ip, port=22000):  # initialisation de l'ip, port
        threading.Thread.__init__(self)
        self.IP = ip
        self.PORT = port
        self.connectedList = {}  # {'adresse':connexion} creation du dictionnaire qui comporte l'adresse et le socket connexion d'un appareil
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # création du socket
        # self.mySocket.settimeout(0.2)		#timeout pour ne pas blocquer le while plus tard
        self.serverALive = True  # activation du while

    def run(self):  # methode a lancer pour tout initialiser
        print('serveur start')

        try:
            self.mySocket.bind((self.IP, self.PORT))  # bind du socket sur l'ip et le port
        except Exception as e:
            print(e)
            return False

        while self.serverALive:  # tant que le serveur est en vie, 
            try:
                self.mySocket.listen(10)
                connexion, adresse = self.mySocket.accept()  # connexion : socket de comunication, addresse liste [ip, port]
                self.connectedList[
                    adresse[0]] = connexion  # enregistre dans le dico le socket de connexion avec l'adresse en clée
                threadReception(self, adresse[0],
                                connexion).start()  # on lance le thread de reception pour chaque connexion
            except Exception as e:
                print(e)

    def stop(self):  # lorsqu'on étein la table, on etein le serveur
        self.serverALive = False
        self.mySocket.close()
        print('serveur deconecter')

    def getConnected(self):  # renvoie la liste des appareils connectés (clée du dico)
        lis = []
        for i in self.connectedList:
            lis.append(i)
        return lis

    def send(self, appareil, message):  # méthode pour envoyer un message à l'adresse choisie
        try:
            self.connectedList[appareil].send(message.encode('utf8'))  # envoi du message
        except Exception as e:
            print(e)
            print('appareil faux/ pb de connexion')


a = serveur('localhost', 8000)
a.start()
while 1:
    listen = a.getConnected()
    if len(listen) > 0:
        listen = listen[0]
        msg = input('> ')
        a.send(listen, msg)