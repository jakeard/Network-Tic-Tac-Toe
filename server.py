import socket
import threading
# "Documents\BYUI Semester 3\Applied Programming\w07\sprint3"

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "disconnected"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)

def send_message(msg, clients):
    for conn in clients:
        conn.send(msg.encode(FORMAT))



def handle_client(conn, addr, clients):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            send_message(msg, clients)
            # conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    clients = []
    s.listen(2)
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        t = threading.Thread(target=handle_client, args=(conn, addr, clients))
        t.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()