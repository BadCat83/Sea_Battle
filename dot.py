from exceptions import IncorrectCoordinates


class Dot:
    """This class describes state of the dot on the game-board. X is the horizontal coordinate.
    Y is the vertical coordinate."""

    def __init__(self, x=None, y=None):
        if x and y and all(map(self.check_coords, (x, y))):
            self.x = x
            self.y = y
        else:
            raise IncorrectCoordinates((x, y))

        self._state = {'empty': True, 'ship': False, 'forbidden': False, 'hit': False, 'miss': False}

    def __eq__(self, other):
        if not isinstance(other, Dot):
            raise TypeError("Right operand must be Dot class!")
        if self.x == other.x and self.y == other.y:
            return True
        return False

    # Check if the coordinates are correct
    @staticmethod
    def check_coords(value):
        if 0 < value <= 6:
            return True
        return False

    # Get dot state
    @property
    def state(self):
        for key, value in self._state.items():
            if value:
                return key

    # Get coordinates of the dot
    @property
    def coords(self):
        return self.x, self.y

    # Set dot state
    @state.setter
    def state(self, changed_key):
        for key, value in self._state.items():
            if key == changed_key:
                self._state[key] = True
            else:
                self._state[key] = False
        if not any(self._state.values()):
            raise ValueError("Некорректное значение _state")

    # Set coordinates to the dot
    @coords.setter
    def coords(self, coords):
        if all(map(self.check_coords, coords)):
            self.x, self.y = (_ for _ in coords)
        else:
            raise IncorrectCoordinates(coords)

    @staticmethod
    def print_help():
        print("x - is a horizontal coordinate, y - is a vertical coordinate")


if __name__ == '__main__':
    dot = Dot(2, 2)
    dot.coords = 3, 3
    dot2 = Dot(3, 4)
    print(dot == dot2)
    dot3 = Dot(2, 4)
    dot3.state = 'ship'
    print(dot3.state, dot.state)
