import time
import socket
import pickle
HOST = "127.0.0.1"
PORT = 65123
HEADER = 10
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    # s.sendall(b"hola mundo")
    names = [100,"Maria","Rodrigo","","Juan","Nabucodonosor"]
    data_serial = pickle.dumps(names)
    data_len = str(len(data_serial))
    data = bytes(f'{data_len:{HEADER}}',"utf-8") + data_serial
    print(data)
    s.send(data)
    '''
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
'''