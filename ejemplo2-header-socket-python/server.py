import socket
import time

HOST = "127.0.0.1"
PORT = 65123
HEADER = 10
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    con, addr = s.accept()
    try:
        with con:
            print(f"Connectado a {addr[0]}:{addr[1]}")
            while True:
                data_len = con.recv(HEADER)
                print(f"len: {data_len}")
                if not data_len:
                    break
                else:
                    data = con.recv(int(data_len))
                    strData = data.decode('utf-8')
                    print(strData)
                # con.sendall(data)
    except KeyboardInterrupt:
        pass

print("Cerrando conexión")
            