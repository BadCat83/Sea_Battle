from exceptions import IncorrectCoordinates, ShotError, CourseError
from ship import *


class Board:
    """This class describes game-board for both players human and AI"""
    _board_size = 6  # It means 6x6

    def __init__(self):
        self.board = [[Dot(x, y) for x in range(1, self._board_size + 1)] for y in range(1, self._board_size + 1)]
        self.ships = []
        self.hid = False
        # self._alive_ships = {'cruiser': 1, 'destroyer': 2, 'boat': 4}

    # Resets the board
    def reinitialize_board(self):
        self.__init__()

    def get_ship(self, dot):
        for ship in self.ships:
            if dot in ship.dots:
                return ship

    # Add ship depending on its type, check the course, coordinates.
    def add_ship(self, *args):
        ship_type, x, y, course = args
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
        self.contour(self.ships[-1])

    # Outlining the ship
    def contour(self, ship):
        for dot in ship.dots:
            x, y = map(lambda v: v - 1, dot.coords)
            dots_index = [(x, y - 1), (x + 1, y - 1),
                          (x + 1, y), (x + 1, y + 1),
                          (x, y + 1), (x - 1, y + 1),
                          (x - 1, y), (x - 1, y - 1,)]
            for val in dots_index.copy():
                if not 0 <= val[0] < 6 or not 0 <= val[1] < 6:
                    dots_index.remove(val)
            for index in dots_index:
                if self.board[index[1]][index[0]].state == 'empty':
                    self.board[index[1]][index[0]].state = 'forbidden'

    # Drawing the board
    def show(self):
        if not self.hid:
            print('\r\r')
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

    # Checks weather the ship placed out of the board or not
    @staticmethod
    def out(x, y):
        if not all(map(Dot.check_coords, (x, y))):
            raise IncorrectCoordinates((x, y))
        return True

    # Makes a shot for player. Shot for Ai logic in player.py. Maybe later I'll make a refactoring
    def shot(self, x, y, board):
        if not self.out(x, y):
            raise IncorrectCoordinates((x, y))
        own_state = board.board[y - 1][x - 1].state
        if own_state == "miss" or own_state == "forbidden":
            raise ShotError
        if (target_dot := self.board[y - 1][x - 1]).state == 'ship':
            print("Hit!")
            ship = self.get_ship(target_dot)
            if not ship.decrease_hit_points():
                self.ships.remove(ship)
                print(f"The {ship.get_name()} is destroyed")
                board.contour(ship)
            return True
        return False

    @staticmethod
    def print_help():
        Board().show()
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
