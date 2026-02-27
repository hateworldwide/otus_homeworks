import math
import pytest

from scr.circle import Circle
from scr.rectangle import Rectangle
from scr.square import Square
from scr.triangle import Triangle


@pytest.mark.parametrize("radius",
                         [-1, 0])
def test_negative_circle(radius):
    with pytest.raises(ValueError):
        Circle(radius)

@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(2, -1, 2),
                          (0, 3, 1),
                          (1, 3, 9)])
def test_negative_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

@pytest.mark.parametrize(("side_a", "side_b"),
                         [(2, -1),
                          (0, 3)])
def test_negative_rectangle(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("side",
                         [-1, 0])
def test_negative_square(side):
    with pytest.raises(ValueError):
        Square(side)

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(5, 4, 3, 6)])
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area, f"Triangle area should be {area} if its sides are: {side_a}, {side_b}, {side_c}"

@pytest.mark.parametrize(("side", "area"),
                         [(5, 25)])
def test_square_area(side, area):
    s = Square(side)
    assert s.get_area == area, f"Square area should be {area} if its side is {side}"

@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(5, 4, 20)])
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f"Rectangle area should be 20 if its sides are: 5, 4"

@pytest.mark.parametrize(("radius"),
                         [5])
def test_circle_area(radius):
    c = Circle(radius)
    assert c.get_area == math.pi * radius * radius, f"Circle area with radius {radius} should be math.pi * {radius} * {radius}"

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [(5, 4, 3, 12)])
def test_triangle_perimeter(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == area, f"Triangle perimeter should be {area} if its sides are: {side_a}, {side_b}, {side_c}"

@pytest.mark.parametrize(("side", "area"),
                         [(5, 20)])
def test_square_perimeter(side, area):
    s = Square(side)
    assert s.get_perimeter == area, f"Square perimeter should be 20 if its side is 5"


@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [(5, 4, 18)])
def test_rectangle_perimeter(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter == area, f"Rectangle perimeter should be {area} if its sides are: {side_a}, {side_b}"

@pytest.mark.parametrize(("radius"),
                         [5])
def test_circle_perimeter(radius):
    c = Circle(radius)
    assert c.get_perimeter == math.pi * 2 * radius, f"Circle perimeter with side 5 should be 2 * math.pi * {radius}"

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "radius"),
                         [(5, 4, 3, 6)])
def test_circle_add_triangle(side_a, side_b, side_c, radius):
    c = Circle(radius)
    t = Triangle(side_a, side_b, side_c)
    assert c.add_area(t) == c.get_area + t.get_area, f"Result area should be {c.get_area()} + {t.get_area()}"

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "side_e"),
                         [(5, 4, 3, 6, 2)])
def test_triangle_add_rectangle(side_a, side_b, side_c, side_d, side_e):
    t = Triangle(side_a, side_b, side_c)
    r = Rectangle(side_d, side_e)
    assert t.add_area(r) == t.get_area + r.get_area, f"Result area should be {t.get_area()} + {r.get_area()}"

@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(2, 1, 2)])
def test_rectangle_add_square(side_a, side_b, side_c):
    r = Rectangle(side_a, side_b)
    s = Square(side_c)
    assert r.add_area(s) == s.get_area + r.get_area, f"Result area should be {s.get_area() + r.get_area()}"

@pytest.mark.parametrize(("side", "radius"),
                         [(5, 4)])
def test_square_add_circle(side, radius):
    s = Square(side)
    c = Circle(radius)
    assert s.add_area(c) == s.get_area + c.get_area, f"Result area should be {s.get_area() + c.get_area()}"
