import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnected"
SERVER = '10.49.180.193'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


class Game:
    def __init__(self):
        self.positions = [x for x in range(1, 10)]
    
    def set_symbol(self, symbol):
        self.symbol = symbol
    
    def set_turn(self, turn):
        if turn == '0':
            self.turn = False
        elif turn == '1':
            self.turn = True

    def run_game(self):
        if self.turn == True:
            self.show_board()
            self.get_user_input()

    def receive_user_input(self, spot):
        if spot in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if self.symbol == 'X':
                self.update_board(int(spot) - 1, 'O')
            else:
                self.update_board(int(spot) - 1, 'X')
            self.turn = True
            self.run_game()

    def pass_user_input(self, spot):
        send(spot)
        self.turn = False

    def show_board(self):
        print(f'\n {self.positions[0]} | {self.positions[1]} | {self.positions[2]} ')
        print('---+---+---')
        print(f' {self.positions[3]} | {self.positions[4]} | {self.positions[5]} ')
        print('---+---+---')
        print(f' {self.positions[6]} | {self.positions[7]} | {self.positions[8]} \n')

    def update_board(self, spot, opponent_symbol=None):
        if opponent_symbol is not None:
            self.positions[spot] = opponent_symbol
        else:
            self.positions[spot] = self.symbol

    def get_user_input(self):
        finished = False
        while not finished:
            try:
                spot = int(input('Where would you like to go? '))
                if spot > 9 or spot < 1 or self.positions[spot - 1] not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    print('Not a valid number!')
                else:
                    self.update_board(spot - 1)
                    self.show_board()
                    finished = True
            except:
                print('Not a valid number!')
        self.pass_user_input(str(spot))




def start_game(game):
    game.run_game()

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    count = 0
    game = Game()
    while True:
        if count != 0:
            print('Waiting for opponent...')
        msg = client.recv(HEADER).decode(FORMAT)
        if msg:
            if count != 0:
                game.receive_user_input(msg)
            else:
                game.set_symbol(msg[0])
                game.set_turn(msg[1])
                start_game(game)
                count += 1

t = threading.Thread(target=receive)
t.start()