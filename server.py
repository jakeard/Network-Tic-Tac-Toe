import socket
import threading
# cd "Documents\BYUI Semester 3\Applied Programming\w07\sprint3"

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

def send_client_symbol(conn, symbol):
    conn.send(symbol.encode(FORMAT))

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
    symbols = ['X', 'O']
    s.listen(2)
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        send_client_symbol(conn, symbols[0])
        t = threading.Thread(target=handle_client, args=(conn, addr, clients))
        t.start()
        try:
            del symbols[0]
        except:
            print('[ERROR] Too many players')
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()