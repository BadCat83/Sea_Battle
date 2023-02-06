from ship import *


class Board:
    """This class describes game-board for both players human and AI"""
    _board_size = 6  # It means 6x6

    def __init__(self):
        self.board = [[Dot(x, y) for x in range(1, self._board_size + 1)] for y in range(1, self._board_size + 1)]
        self.ships = []
        self.hid = False
        self.alive_ships = {'cruiser': 1, 'destroyer': 2, 'boat': 4}

    def add_ship(self, ship_type):
        self.ships.append(ship_type)

    def contour(self):
        pass

    def show(self):
        if not self.hid:
            print(' ' * 6, end='')
            print(f"{' ' * 5}".join([str(_) for _ in range(1, self._board_size + 1)]))
            print(' ' * 3, end='')
            print('-' * 37)
            for index, y_coord in enumerate(self.board, 1):
                print(index, end='')
                for x_coord in y_coord:
                    if x_coord.state == 'empty':
                        symb = 'O'
                    elif x_coord.state == 'ship':
                        symb = '#'
                    elif x_coord.state == 'forbidden':
                        symb = '!'
                    else:
                        symb = 'X'
                    print(f"  |  {symb}", end='')
                print('  |')
                print(' ' * 3, end='')
                print('-' * 37)

    def out(self):
        pass

    def shot(self):
        pass


if __name__ == '__main__':
    game_board = Board()
    game_board.show()
    ship = Cruiser()
    ship.dots = 1, 2, 1
    game_board.add_ship(ship)
    for ship in game_board.ships:
        for dot in ship.dots:
            print(dot.coords)
