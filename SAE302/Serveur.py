import socket
import os
import platform


def data():
    reply = ""  # message serveur
    data = ""  # message client
    while data != "kill":
        server_socket = socket.socket()
        server_socket.bind(('127.0.0.1', 8111))
        server_socket.listen(1)
        while data != "kill" and data != "reset":
            conn, address = server_socket.accept()
            while data != "disconnect" and data != "kill" and data != "reset":
                data = conn.recv(1024).decode()
                print("Client : ", data)
                conn.send(data.encode())
                if data == "OS":
                    print("GEGE")
                    conn.send(reply.encode())
            conn.close()
        server_socket.close()  # fermeture serveur


if __name__ == '__main__':
    data()