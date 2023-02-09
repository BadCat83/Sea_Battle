from board import Board
from exceptions import ShotError


class Player:

    def __init__(self):
        self.own_board = Board()
        self.opponent_board = Board()

    def place_ships(self):
        pass

    def ask(self):
        pass

    def move(self):
        self.opponent_board.show()
        self.ask()

    @staticmethod
    def print_help_coordinates():
        print("Coordinates must be in this format - x,y \nAnd ranging from 1 to 6 inclusive")


class User(Player):

    def ask(self):
        while True:
            try:
                x, y = [int(val) for val in input("Where do you want to shoot?"
                                                  " Please, input two coordinates separated by comma: "
                                                  "x - horizontal, y - vertical: ").split(',')]
                for every in self.own_board, self.opponent_board:
                    every.shot(x, y)

            except ShotError as se:
                print(se)
                continue

            except Exception as e:
                print(e)
                Player().print_help_coordinates()
                continue
            else:
                break

    @staticmethod
    def input_coords(msg):
        return [int(val) for val in input(msg).split(',')]

    def place_ships(self):
        self.own_board.print_help()
        while True:
            try:
                print(
                    "For every ship you need to enter starting position (x,y) and course 0 - vertical, 1 - horizontal")
                x, y, course = self.input_coords("Please, place the cruiser first: ")
                self.own_board.add_ship('cruiser', x, y, course)
                self.own_board.show()
                for i, _ in enumerate(range(2), 1):
                    x, y, course = self.input_coords(f"Please, place {i} destroyer: ")
                    self.own_board.add_ship('destroyer', x, y, course)
                    self.own_board.show()
                for i, _ in enumerate(range(4), 1):
                    x, y = self.input_coords(f"Please, place {i} boat: ")
                    self.own_board.add_ship('boat', x, y)
                    self.own_board.show()

            except Exception as e:
                print(e)


if __name__ == '__main__':
    player = User()
    # player.ask()
    # player.opponent_board.show()
    # player.ask()
    player.place_ships()
