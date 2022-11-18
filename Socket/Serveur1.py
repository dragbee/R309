import socket

def data():
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    reply = ""  #message serveur
    data = ""   #message client
    while reply != "arret" and data != "arret":
        conn, address = server_socket.accept()
        while reply != "bye" and data !="bye" and reply != "arret" and data != "arret":
            data = conn.recv(1024).decode()
            if data == "bye":
                conn.send("bye".encode())
            print("Client : ", data)
            reply = input("Server : ")
            conn.send(reply.encode())
        conn.close()  # fermeture connexion serveur, client
    server_socket.close()  # fermeture serveur


if __name__ == '__main__':
        data()

