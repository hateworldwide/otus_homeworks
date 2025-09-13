import math

from scr.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if side_a <=0 or side_b <= 0:
            raise ValueError("Sides of rectangle must be positive")
        self.side_a = side_a
        self.side_b = side_b


    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        return self.side_a * self.side_b

