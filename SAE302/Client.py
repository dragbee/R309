import socket
import threading

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
def client(client_socket):
    print("t1 start")
    while True:
        msgclient = input("Client : ")
        client_socket.send(msgclient.encode())

def serv(client_socket):
    print('t2 start')
    while True:
        msgserv = client_socket.recv(1024).decode()
        print(msgserv)

t1 = threading.Thread(target=client)
t2 = threading.Thread(target=serv)
t1.start()
t2.start()
t1.join()
t2.join()


if __name__ == '__main__':
    try:
        client_socket = socket.socket()
        client_socket.connect(('127.0.0.1', 8111))
        client(client_socket)
        serv(client_socket)
    except ConnectionAbortedError:
        print("Serveur déconnecté...")
"""


