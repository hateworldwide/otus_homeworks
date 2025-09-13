import math
import pytest

from scr.circle import Circle
from scr.rectangle import Rectangle
from scr.square import Square
from scr.triangle import Triangle

def test_negative_triangle_negative_side():
    with pytest.raises(ValueError):
        Triangle(4, -1, 6)

def test_negative_triangle_zero_side():
    with pytest.raises(ValueError):
        Triangle(0, 3, 6)

def test_negative_triangle_too_big_side():
    with pytest.raises(ValueError):
        Triangle(1, 3, 6)

def test_negative_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(-1)

def test_negative_circle_zero_radius():
    with pytest.raises(ValueError):
        Circle(0)

def test_negative_rectangle_negative_side():
    with pytest.raises(ValueError):
        Rectangle(-2, 2)

def test_negative_rectangle_zero_side():
    with pytest.raises(ValueError):
        Rectangle(0, 2)

def test_negative_square_negative_side():
    with pytest.raises(ValueError):
        Square(-1)

def test_triangle_area():
    t = Triangle(5, 4, 3)
    assert t.get_area == 6, f"Triangle area should be 6 if its sides are: 5, 4, 3"

def test_square_area():
    s = Square(5)
    assert s.get_area == 25, f"Square area should be 25 if its side is 5"

def test_rectangle_area():
    r = Rectangle(5, 4)
    assert r.get_area == 20, f"Rectangle area should be 20 if its sides are: 5, 4"

def test_circle_area():
    c = Circle(5)
    assert c.get_area == math.pi * 5 * 5, f"Circle area with side 5 should be math.pi * 5 * 5"

def test_triangle_perimeter():
    t = Triangle(5, 4, 3)
    assert t.get_perimeter == 12, f"Triangle perimeter should be 12 if its sides are: 5, 4, 3"

def test_square_perimeter():
    s = Square(5)
    assert s.get_perimeter == 20, f"Square perimeter should be 20 if its side is 5"

def test_rectangle_perimeter():
    r = Rectangle(5, 4)
    assert r.get_perimeter == 18, f"Rectangle perimeter should be 18 if its sides are: 5, 4"

def test_circle_perimeter():
    c = Circle(5)
    assert c.get_perimeter == math.pi * 2 * 5, f"Circle perimeter with side 5 should be 2 * math.pi * 5"

def test_circle_add_triangle():
    c = Circle(5)
    t = Triangle(5, 4, 3)
    assert c.add_area(t) == c.get_area + t.get_area, f"Result area should be {c.get_area()} + {t.get_area()}"

def test_triangle_add_rectangle():
    t = Triangle(5, 4, 3)
    r = Rectangle(5, 4)
    assert t.add_area(r) == t.get_area + r.get_area, f"Result area should be {t.get_area()} + {r.get_area()}"

def test_rectangle_add_square():
    r = Rectangle(5, 4)
    s = Square(5)
    assert r.add_area(s) == s.get_area + r.get_area, f"Result area should be {s.get_area() + r.get_area()}"

def test_square_add_circle():
    s = Square(5)
    c = Circle(5)
    assert s.add_area(c) == s.get_area + c.get_area, f"Result area should be {s.get_area() + c.get_area()}"