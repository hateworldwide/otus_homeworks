import math

from scr.figure import Figure


class Circle(Figure):

    def __init__(self, side):
        if side <=0:
            raise ValueError("side of circle must be positive")
        self.side = side



    @property
    def get_perimeter(self):
        return 2 * math.pi * self.side

    def get_area(self):
        return math.pi * self.side * self.side