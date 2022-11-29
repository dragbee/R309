"""
import platform

print(platform.uname())
"""
from Client import server_socket

host = input("hostname : ")
port = input("port : ")
serv = server_socket(host, port)
serv.connect()
rep = serv.send()
if rep == "":
    print("serveur no connecté")
else:
    print(rep)
