from dot import Dot


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

    def get_name(self):
        return self.name

    @property
    def dots(self):
        return self._dots

    @dots.setter
    def dots(self, data):
        x, y, self.course = (_ for _ in data)
        if self.course:
            self._dots = [Dot(x, y) for x in range(x, x + self.length)]
        else:
            self._dots = [Dot(x, y) for y in range(y, y + self.length)]


class Boat(Ship):
    def __init__(self):
        self.length = self.hit_points = 1
        self.name = 'boat'


class Destroyer(Ship):
    def __init__(self):
        self.length = self.hit_points = 2
        self.name = 'destroyer'


class Cruiser(Ship):
    def __init__(self):
        self.length = self.hit_points = 3
        self.name = 'cruiser'


if __name__ == '__main__':
    ship = Cruiser()
    ship.dots = 1, 2, 1
    for dot in ship.dots:
        print(dot.coords)
