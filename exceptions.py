class BoardOutException(Exception):
    def __str__(self):
        return 'The ship with this coordinates will be placed out of the board'


class IncorrectCoordinates(Exception):
    def __init__(self, coords):
        self.message = coords

    def __str__(self):
        return f'{self.message} are incorrect coordinates!'

class TryException(Exception):

    def __str__(self):
        return "Too many attempts to place the ship"


class ShotError(Exception):

    def __str__(self):
        return 'You has already shot to this position'


class CourseError(Exception):

    def __init__(self, course):
        self.course = course

    def __str__(self):
        return f"Course {self.course} is incorrect"


if __name__ == '__main__':
    # raise BoardOutException((7, 8))
    raise ShotError((1, 1))
