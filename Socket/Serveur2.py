import socket
import threading

def envoie(server_socket):
    return


def reception(server_socket):
    while reply != "arret" and data != "arret":
        conn, address = server_socket.accept()
        while reply != "bye" and data !="bye" and reply != "arret" and data != "arret":
            data = conn.recv(1024).decode()
            if data == "bye":
                conn.send("bye".encode())
            print("Client : ", data)
            reply = input("Server : ")
            conn.send(reply.encode())


if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    conn, address = server_socket.accept()