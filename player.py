import random
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

    def ask(self, board):
        pass

    def move(self, board):
        self.opponent_board.show()
        self.ask(board)

    @staticmethod
    def print_help_coordinates():
        print("Coordinates must be in this format - x,y \nAnd ranging from 1 to 6 inclusive")


class User(Player):

    def ask(self, enemy_board):
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

    def __init__(self):
        super().__init__()
        # self.possible_shots = self.opponent_board.board.copy()
        self.next_shots = []
        self.last_hit = None

    @staticmethod
    def generate_number(top):
        if top == 1:
            return randint(0, top)
        return randint(1, top)

    def add_ship(self, ship_type):
        tries = 0
        print(f"\rTrying to place {ship_type}")
        while True:
            tries += 1
            if tries > 300:
                print("\rIt didn't work, I'll try again...")
                raise TryException
            elif tries % 10 == 0:
                print("\rI'm still calculating", end='')
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
                for _ in range(2):
                    self.add_ship('destroyer')
                for _ in range(4):
                    self.add_ship('boat')
            except TryException:
                self.own_board.reinitialize_board()
            else:
                # self.own_board.show()
                print("\rI'm ready :)")
                break

    def ask(self, enemy_board):
        possible_shots = [dot for dots in self.opponent_board.board for dot in dots if dot.state == 'empty']
        if not self.next_shots:
            random_dot = random.choice([_ for _ in possible_shots if _])
        else:
            random_dot = random.choice(self.next_shots.copy())
            self.next_shots.remove(random_dot)
        x, y = random_dot.coords
        target_dot = enemy_board.board[y - 1][x - 1]
        ai_dot = self.opponent_board.board[y - 1][x - 1]
        if target_dot.state == 'ship':
            ai_dot.state = target_dot.state = 'hit'
            ship = enemy_board.get_ship(random_dot)
            if not ship.decrease_hit_points():
                player.own_board.ships.remove(ship)
                self.next_shots.clear()
                self.last_hit = None
                self.opponent_board.contour(ship)
            else:
                self.fill_next_shots(target_dot)
                self.last_hit = target_dot
            # self.possible_shots[random_dot.coords[1] - 1].remove(random_dot)
            return True
        else:
            ai_dot.state = target_dot.state = 'miss'
            # self.possible_shots[random_dot.coords[1] - 1].remove(random_dot)
            return False

    def fill_next_shots(self, dot):
        x, y = (val - 1 for val in dot.coords)
        if self.last_hit:
            self.next_shots.clear()
            if self.last_hit.coords[0] == x + 1:
                if not y - self.last_hit.coords[1]:
                    possible_dots = [(y + 1, x), (y - 2, x)]
                else:
                    possible_dots = [(y - 1, x), (y + 2, x)]
            else:
                if not x - self.last_hit.coords[0]:
                    possible_dots = [(y, x + 1), (y, x - 2)]
                else:
                    possible_dots = [(y, x - 1), (y, x + 2)]
        else:
            possible_dots = [(y - 1, x), (y, x + 1),
                             (y + 1, x), (y, x - 1)]
        for y, x in possible_dots.copy():
            if 0 <= y < 6 and 0 <= x < 6:
                if (t_dot := self.opponent_board.board[y][x]).state == 'empty':
                    self.next_shots.append(t_dot)

    # self.opponent_board.show()


if __name__ == '__main__':
    # player = User()
    # player.ask()
    # player.opponent_board.show()
    # player.ask()
    ai = Ai()
    ai2 = Ai()
    ai2.place_ships()
    ai2.own_board.show()
    turn = 0
    while True:
        turn += 1
        if not ai.ask(ai2.own_board):
            # Передача хода
            continue
        else:
            ai.opponent_board.show()
            if not ai2.own_board.ships:
                print(f"It's a win, it takes {turn} turns")
                break
