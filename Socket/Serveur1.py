import socket

def data(conn):
    data = conn.recv(1024).decode()
    print("Client : ", data)
    reply = input("Server : ")
    conn.send(reply.encode())

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while True:
        data(conn)
    conn.close()
