# import arcade

class Game:
    def __init__(self):
        self.positions = [x for x in range(1, 10)]
        self.turn = True
        # self.symbol = symbol

    def show_board(self):
        print(f'\n {self.positions[0]} | {self.positions[1]} | {self.positions[2]} ')
        print('---+---+---')
        print(f' {self.positions[3]} | {self.positions[4]} | {self.positions[5]} ')
        print('---+---+---')
        print(f' {self.positions[6]} | {self.positions[7]} | {self.positions[8]} \n')

    def update_board(self, spot):
        self.positions[spot] = 'X' # self.symbol
        # self.turn = False

    def get_user_input(self):
        if self.turn:
            while self.turn:
                try:
                    spot = int(input('Where would you like to go? '))
                    if spot > 9 or spot < 1 or self.positions[spot - 1] not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                        print('Not a valid number!')
                    else:
                        self.update_board(spot - 1)
                        self.show_board()
                except:
                    print('Not a valid number!')

                
                
            # self.pass_user_input(spot)

    def pass_user_input(self):
        pass

    def receive_user_input(self, spot):
        pass

game = Game()

while True:
    game.show_board()
    game.get_user_input()