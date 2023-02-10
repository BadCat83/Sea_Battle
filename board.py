from functools import reduce

from exceptions import IncorrectCoordinates, ShotError, CourseError
from ship import *


class Board:
    """This class describes game-board for both players human and AI"""
    _board_size = 6  # It means 6x6

    def __init__(self):
        self.board = [[Dot(x, y) for x in range(1, self._board_size + 1)] for y in range(1, self._board_size + 1)]
        self.ships = []
        self.hid = False
        self._alive_ships = {'cruiser': 1, 'destroyer': 2, 'boat': 4}

    def reinitialize_board(self):
        self.__init__()


    def get_alive(self, name):
        return self._alive_ships[name]

    def reduce_alive(self, name):
        self._alive_ships[name] -= 1

    def add_ship(self, *args):
        ship_type, x, y, course = (_ for _ in args)
        if not 0 <= course <= 1:
            raise CourseError(course)
        if ship_type == 'boat':
            ship_type = Boat()
        elif ship_type == 'destroyer':
            ship_type = Destroyer()
        else:
            ship_type = Cruiser()
        ship_type.dots = x, y, course
        temp_dots = []
        for dot in ship_type.dots:
            x, y = (_ for _ in dot.coords)
            if (target_dot := self.board[y - 1][x - 1]).state == 'empty':
                temp_dots.append(target_dot)
            else:
                raise IncorrectCoordinates(dot.coords)
        for dot in temp_dots:
            dot.state = 'ship'
        self.ships.append(ship_type)
        self.contour()

    def contour(self):
        for i, dots_list in enumerate(self.board):
            for j, dot in enumerate(dots_list):
                if dot.state == 'ship':
                    dots_index = [(i - 1, j - 1), (i - 1, j),
                                  (i - 1, j + 1), (i, j - 1),
                                  (i, j + 1), (i + 1, j - 1),
                                  (i + 1, j), (i + 1, j + 1)]
                    for val in dots_index.copy():
                        if not 0 <= val[0] < 6 or not 0 <= val[1] < 6:
                            dots_index.remove(val)
                    for index in dots_index:
                        if self.board[index[0]][index[1]].state == 'empty':
                            self.board[index[0]][index[1]].state = 'forbidden'

    def show(self):
        if not self.hid:
            print('\n')
            print(' ' * 6, end='')
            print(f"{' ' * 5}".join([str(_) for _ in range(1, self.board_size + 1)]))
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
                    elif x_coord.state == 'miss':
                        symb = '0'
                    else:
                        symb = 'X'
                    print(f"  |  {symb}", end='')
                print('  |')
                print(' ' * 3, end='')
                print('-' * 37)

    @staticmethod
    def out(x, y):
        if not all(map(Dot.check_coords, (x, y))):
            raise IncorrectCoordinates((x, y))
        return True

    def shot(self, x, y):
        if not self.out(x, y):
            raise IncorrectCoordinates((x, y))
        target_dot = Dot(x, y)
        for dot in [dot for dots in self.board for dot in dots]:
            if target_dot.coords == dot.coords:
                if dot.state == 'ship':
                    dot.state = 'hit'
                    for target_ship in self.ships:
                        if dot in ship.dots:
                            target_ship.decrease_hit_points()
                        if target_ship.get_hit_points() == 0:
                            self.reduce_alive(target_ship.get_name())
                elif dot.state == 'hit' or dot.state == 'miss':
                    raise ShotError
                else:
                    dot.state = 'miss'
                break

    @staticmethod
    def print_help():
        tmp = Board()
        tmp.show()
        print(f"This is your board. You need to place ships on it."
              f" You have got a cruiser, two destroyers and four boats")
        Ship().print_help()
        Boat().print_length_help()
        Destroyer().print_length_help()
        Cruiser().print_length_help()
        print("\n. - empty cell\n+ - a cell with the ship or a part of the ship"
              "\nF - a forbidden cell, there is no way to place ship in there, but you can try it )"
              "\n0 - miss marks as zero\nX - hit marks as X")

    @property
    def board_size(self):
        return self._board_size


if __name__ == '__main__':
    game_board = Board()
    # game_board.show()
    ship = Cruiser()
    ship.dots = 3, 3, 0
    game_board.add_ship(ship)
    game_board.shot(1, 2)

    # ship2 = Destroyer()
    # ship2.dots = 5, 1, 0
    # game_board.add_ship(ship2)
    Board.print_help()
