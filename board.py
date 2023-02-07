from functools import reduce

from exceptions import IncorrectCoordinates
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
        dots_list = [dot for dots in self.board for dot in dots]
        for index, dot in enumerate(dots_list):
            if dot in ship_type.dots:
                if dot.state == 'empty':
                    dot.state = 'ship'
                else:
                    raise IncorrectCoordinates(dot.coords)
        self.contour(dots_list)

    def contour(self, dots):
        for i, dots_list in enumerate(self.board):
            for j, dot in enumerate(dots_list):
                if dot.state == 'ship':
                    dots_index = [(i-1, j-1), (i-1, j),
                                  (i-1, j+1), (i, j-1),
                                  (i, j+1), (i+1, j-1),
                                  (i+1, j), (i+1, j+1)]
                    for val in dots_index.copy():
                        if not 0 <= val[0] < 6 or not 0 <= val[1] < 6:
                            dots_index.remove(val)
                    for index in dots_index:
                        if self.board[index[0]][index[1]].state == 'empty':
                            self.board[index[0]][index[1]].state = 'forbidden'


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
                        symb = '.'
                    elif x_coord.state == 'ship':
                        symb = '+'
                    elif x_coord.state == 'forbidden':
                        symb = 'F'
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
    #game_board.show()
    ship = Cruiser()
    ship.dots = 1, 1, 0
    game_board.add_ship(ship)
    # ship2 = Destroyer()
    # ship2.dots = 5, 1, 0
    # game_board.add_ship(ship2)
    game_board.show()

