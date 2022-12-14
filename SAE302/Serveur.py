import socket
import os
import platform
import subprocess
import psutil


def data():
    reply = ""  # message serveur
    data = ""  # message client
    while data != "kill":
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8111))
        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while data != "kill" and data != "reset":
            conn, address = server_socket.accept()
            print('connecté')
            while data != "disconnect" and data != "kill" and data != "reset":
                data = conn.recv(1024).decode()
                print("Client : ", data)

                if data == "OS" or data == "IP" or data == "NAME":
                    if data == "OS":
                        cmd = "ver"

                    elif data == "IP":
                        cmd = "ipconfig | findstr IPv4"

                    else:  # data == "NAME"
                        cmd = "hostname"

                    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850',
                                         shell=True)
                    cmd = p.stdout.read()
                    conn.send(cmd.encode())

                elif data == "RAM" or data == "CPU":
                    if data == "RAM":
                        ram = f"total : {round(((psutil.virtual_memory()[0]) / 1000000000),2)} Go\n available : {round(((psutil.virtual_memory()[1]) / 1000000000),2)} Go\n used : {psutil.virtual_memory().percent} %"
                        conn.send(ram.encode())
                    else: #data == "CPU"
                        cpu = f"used (%) : {psutil.cpu_percent()}"
                        conn.send(cpu.encode())
                else:
                    conn.send(data.encode())

            conn.close()
        server_socket.close()  # fermeture serveur


if __name__ == '__main__':
    data()
