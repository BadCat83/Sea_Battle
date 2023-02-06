class BoardOutException(Exception):
    def __init__(self, coords):
        self.message = coords

    def __str__(self):
        return f'Specified coordinates {self.message} are incorrect'

class IncorrectCoordinates(Exception):
    def __init__(self, coords):
        self.message = coords

    def __str__(self):
        return f'{self.message} are incorrect coordinates!'

class ShotError(Exception):
    def __init__(self, coords):
        self.message = coords

    def __str__(self):
        return f'You has already shot to this position'


if __name__ == '__main__':
    #raise BoardOutException((7, 8))
    raise ShotError((1, 1))
