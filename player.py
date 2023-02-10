from random import randint
from time import sleep

from board import Board
from exceptions import ShotError, TryException, BoardOutException, IncorrectCoordinates


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

    def add_ship(self, msg, ship_type):
        while True:
            try:
                if not ship_type == "boat":
                    x, y, course = self.input_coords(msg)
                else:
                    x, y = self.input_coords(msg)
                    course = 0
                self.own_board.add_ship(ship_type, x, y, course)
                self.own_board.show()
            except Exception as e:
                print(e)
            else:
                break

    def place_ships(self):
        self.own_board.print_help()
        print("For every ship you need to enter starting position (x,y) and course 0 - vertical, 1 - horizontal")
        self.add_ship("Please, place the cruiser first (x,y,course): ", 'cruiser')
        for i, _ in enumerate(range(2), 1):
            self.add_ship(f"Please, place {i} destroyer (x,y,course): ", 'destroyer')
        for i, _ in enumerate(range(4), 1):
            self.add_ship(f"Please, place {i} boat (x,y): ", 'boat')


class Ai(Player):

    @staticmethod
    def generate_number(top):
        if top == 1:
            return randint(0, top)
        return randint(1, top)

    def add_ship(self, ship_type):
        tries = 0
        print(f"Trying to place {ship_type}")
        while True:
            tries += 1
            if tries > 10000:
                raise TryException
            try:
                self.own_board.add_ship(ship_type, *(map(self.generate_number,
                                                         (self.own_board.board_size, self.own_board.board_size,
                                                          1))))
            except (BoardOutException, IncorrectCoordinates):
                print('.', end='')
                sleep(0.1)
            else:
                break

    def place_ships(self):
        print('Calculating... ', end='')
        while True:
            try:
                self.add_ship('cruser')
                self.own_board.show()
                for _ in range(2):
                    self.add_ship('destroyer')
                    self.own_board.show()
                for _ in range(4):
                    self.add_ship('boat')
                    self.own_board.show()
            except TryException:
                print("\nI'm still calculating )", end='')
                self.own_board.reinitialize_board()
            else:
                self.own_board.show()
                break


if __name__ == '__main__':
    player = User()
    # player.ask()
    # player.opponent_board.show()
    # player.ask()
    ai = Ai()
    ai.place_ships()
