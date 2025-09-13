import math

from scr.figure import Figure

class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <=0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides of triangle must be positive")
        if side_a >= side_b + side_c or side_b >= side_c + side_a or side_c >= side_b + side_a:
            raise ValueError("In triangle one side can't be greater than sum of two other sides")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


    @property
    def get_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

    @property
    def get_area(self):
        pp = self.get_perimeter / 2
        return math.sqrt(pp * (pp - self.side_a) * (pp - self.side_b) * ( pp - self.side_c))