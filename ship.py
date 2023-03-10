from dot import Dot
from exceptions import BoardOutException


class Ship:
    """This class describes one of three types of ships. It can be ship that occupied one, two or three cells.
        Course means the heading of the ship, it can be vertical (0) or horizontal (1).
        Bow of the ship as a start position to fill the board. The ship is placed from up to down if course is
        vertical otherwise from right to left"""

    def __init__(self):
        self.length = self.course = None
        # self.bow = Dot()
        self._dots = []
        self.hit_points = None
        self.name = None

    def __eq__(self, other_ship):
        if not isinstance(other_ship, Ship):
            raise TypeError("Right operand must be Ship class!")
        if self._dots == other_ship._dots:
            return True
        return False

    def get_name(self):
        return self.name

    def decrease_hit_points(self):
        self.hit_points -= 1
        return self.hit_points

    @staticmethod
    def print_help():
        print(
            f"A ship is positioned from starting coordinates from up to down or from left to right,"
            f" depending on course.")

    def print_length_help(self):
        print(f"The {self.get_name()}'s length is {self.hit_points}. ", end='')

    @property
    def dots(self):
        return self._dots

    @dots.setter
    def dots(self, data):
        x, y, self.course = (_ for _ in data)
        try:
            if self.course == 1:
                self._dots = [Dot(x, y) for x in range(x, x + self.length)]
            else:
                self._dots = [Dot(x, y) for y in range(y, y + self.length)]
        except Exception:
            raise BoardOutException


class Boat(Ship):
    def __init__(self):
        super().__init__()
        self.length = self.hit_points = 1
        self.name = 'boat'


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.length = self.hit_points = 2
        self.name = 'destroyer'


class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self.length = self.hit_points = 3
        self.name = 'cruiser'


if __name__ == '__main__':
    ship = Destroyer()
    ship.dots = 1, 2, 1
    for dot in ship.dots:
        print(dot.coords)

    ship2 = Boat()
    ship.print_help()
