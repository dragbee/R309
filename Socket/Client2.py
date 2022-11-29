import socket
import threading

def client(client_socket):
    print('t1 start')
    while True:
        msgclient = input("Client : ")
        client_socket.send(msgclient.encode())

def serv(client_socket):
    print('t2 start')
    while True:
        msgserv = client_socket.recv(1024).decode()
        print(msgserv)

t1 = threading.Thread(target=client)
t1.start()
t2 = threading.Thread(target=serv)
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