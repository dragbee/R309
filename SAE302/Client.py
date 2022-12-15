"""
class server_socket():

    def __init__(self, hostname, port):
        self.__hostname = hostname
        self.__port = port
        self.__socket = None

    def isconnected(self):
        return self.__socket != None

    def __connect(self):
        socket = self.__socket.socket()
        self.__socket.connect((self.__hostname, self.__port))

    def __send(self, message):
        if self.isconnected():
            self.__socket.send(message)
            message = self.__socket.receive()
            print(message)
        print("PAS DE CONNEXIONNNNNNNNNNN")

    def close(self):
        socket.close()

    def connect(self):
        threading.Thread(target=self.__connect)

    def send(self):
        threading.Thread(target=self.__send)
        
                
"""

"""
def client(client_socket):
    msgserv = ''
    while msgserv != "disconnect" and msgserv != "kill" and msgserv != "reset":
        msgclient = input("Client : ")
        client_socket.send(msgclient.encode())

        msgserv = client_socket.recv(1024).decode()
        print("Serveur :", msgserv)


if __name__ == '__main__':
    try:
        client_socket = socket.socket()
        client_socket.connect(('127.0.0.1', 8111))
        client(client_socket)
        client_socket.close()
    except ConnectionAbortedError:
        print("Serveur déconnecté...")
"""

import socket, threading, sys


class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.thread = None

    # fonction de connection.
    def connect(self) -> int:
        try:
            self.sock.connect((self.host, self.port))
        except ConnectionRefusedError:
            print("serveur non lancé ou mauvaise information")
            return -1
        except ConnectionError:
            print("erreur de connection")
            return -1
        else:
            print("connexion réalisée")
            return 0

    """ 
        fonction qui gére le dialogue
        -> lance une thread pour la partie reception 
        -> lance une boucle pour la partie emission. arréte si kill, reset ou disconnect
    """

    def dialogue(self):
        msg = ""
        self.thread = threading.Thread(target=self.reception, args=[self.sock, ])
        self.thread.start()
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = self.envoi()
        self.thread.join()
        self.sock.close()

    def envoi(self):
        msg = input("client: ")
        try:
            self.sock.send(msg.encode())
        except BrokenPipeError:
            print("erreur, socket fermée")
        return msg

    """
      thread recepction, la connection étant passée en argument
    """

    def reception(self, conn):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = conn.recv(1024).decode()
            print(msg)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1", 8111)

        client.connect()
        client.dialogue()

