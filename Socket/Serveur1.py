import socket

def data(conn):
    data = conn.recv(1024).decode()
    print("Client : ", data)
    reply = input("Server : ")
    conn.send(reply.encode())


if __name__ == '__main__':
    reply = ""
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    while reply != "arret":
        conn, address = server_socket.accept()
        while reply != "bye":
            data(conn)

    conn.close()
