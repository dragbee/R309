import socket

def data():
    server_socket.listen(1)
    reply = ""  #message serveur
    data = ""   #message client
    conn, address = server_socket.accept()
    while True:
        data = conn.recv(1024).decode()
        print("Client : ", data)
        reply = input("Server : ")
        print(reply)
        conn.send(reply.encode())
        conn.send(data.encode())
    conn.close()  # fermeture connexion serveur, client
    server_socket.close()  # fermeture serveur


if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    data()