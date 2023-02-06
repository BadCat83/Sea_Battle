from dot import Dot


class Ship:
    """This class describes one of three types of ships. It can be ship that occupied one, two or three cells.
        Course means the heading of the ship, it can be vertical (0) or horizontal (1).
        Bow of the ship as a start position to fill the board. The ship is placed from up to down if course is
        vertical otherwise from right to left"""

    def __init__(self):
        self.length = self.course = None
        #self.bow = Dot()
        self._dots = []
        self.hit_points = None

    @property
    def dots(self):
        return self._dots

    @dots.setter
    def dots(self, data):
        x, y, self.course, self.length = (_ for _ in data)
        #self.bow.coords = x, y
        self.hit_points = self.length
        if self.course:
            self._dots = [Dot(x, y) for x in range(x, x + self.length)]



if __name__ == '__main__':
    ship = Ship()
    ship.dots = 1, 4, 1, 3
    for dot in ship.dots:
        print(dot.coords)