# import arcade
import client
# import client.receive

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
        count = 0
        if self.turn == True:
            self.show_board()
            self.get_user_input()
        else:
            print('Waiting for opponent...')

    def receive_user_input(self, spot):
        if spot in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if self.symbol == 'X':
                self.update_board(int(spot) - 1, 'O')
            else:
                self.update_board(int(spot) - 1, 'X')
            self.turn = True
            self.run_game()

    def pass_user_input(self, spot):
        client.Client.send(spot)
        self.turn = False
        self.receive_user_input()

    def show_board(self):
        print(f'\n {self.positions[0]} | {self.positions[1]} | {self.positions[2]} ')
        print('---+---+---')
        print(f' {self.positions[3]} | {self.positions[4]} | {self.positions[5]} ')
        print('---+---+---')
        print(f' {self.positions[6]} | {self.positions[7]} | {self.positions[8]} \n')

    def update_board(self, spot, opponent_symbol=None):
        if opponent_symbol is not None:
            self.positions[spot] = opponent_symbol
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
                    self.pass_user_input(str(spot))
            except:
                print('Not a valid number!')
