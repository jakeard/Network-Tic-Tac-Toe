import socket
import threading
import arcade

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnected"
SERVER = '10.49.180.111'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))

def receive():
    while True:
        msg = client.recv(HEADER).decode(FORMAT)
        if msg:
            # msg_length = int(msg_length)
            # msg = client.recv(msg_length).decode(FORMAT)
            print(msg)

def game():
    pass

t = threading.Thread(target=receive)
t.start()
send('hello world')
