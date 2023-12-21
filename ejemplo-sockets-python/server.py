import socket
import time

HOST = "127.0.0.1"
PORT = 65123

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    con, addr = s.accept()
    
    time.sleep(1)
    with con:
        print(f"Connectado a {addr}:")
        while True:
            data = con.recv(1024)
            if not data:
                break
            con.sendall(data)