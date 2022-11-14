import socket

def data(client_socket):

    message = input("Client : ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("Serveur : ", data)



if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 8111))
    while data != "bye":
        data(client_socket)
    client_socket.close()