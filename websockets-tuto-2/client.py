import socket

PORT = 5050
HEADER = 64
FORMAT = "utf-8"
# SERVER = "192.168.1.23"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))
send("!Hola world") 
send("!Tedible") 
send("!Tedibleeqweqweqwe")
send(DISCONNECT_MESSAGE) 