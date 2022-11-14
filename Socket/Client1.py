import socket

def data():
    message = input("Client : ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    if data != "":
        print("Serveur : ", data)
    if message == "wow":
        client_socket.close()

if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 8111))
    while True:
        data()
    client_socket.close()
