import socket

def data(client_socket):
    message = ""    #message client
    data = ""       #message serveur
    while message != "bye" and data != "bye" and message != "arret" and data != "bye":
        message = input("Client : ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Serveuur : ', data)


if __name__ == '__main__':
    try:
        client_socket = socket.socket()
        client_socket.connect(('127.0.0.1', 8111))
        data(client_socket)
        client_socket.close()
    except ConnectionAbortedError:
        print("Serveur déconnecté...")

