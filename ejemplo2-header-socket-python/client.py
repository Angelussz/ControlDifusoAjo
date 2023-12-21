import time
import socket

HOST = "127.0.0.1"
PORT = 65123
HEADER = 10
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    # s.sendall(b"hola mundo")
    names = [100,"Maria","Rodrigo","","Juan","Nabucodonosor"]
    for name in names:
        # <HEADER ><PAYLOAD>
        strData = str(name)
        data_len = str(len(strData))
        # s.send(data_len.encode("utf-8"))
        # time.sleep(1)
        # data = f"{strData}".encode("utf-8")
        data = f"{data_len:<{HEADER}}{strData}".encode("utf-8")
        s.send(data)
        time.sleep(1)
    # data = s.recv(1024)

# print("Recibido",repr(data))