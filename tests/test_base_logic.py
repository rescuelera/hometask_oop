from math import pi
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


def test_add_area_circle_and_triangle():
    circle = Circle("circle", 5)
    assert circle.name == "circle"
    assert circle.radius == 5
    assert circle.area == 5 * 5 * pi

    triangle = Triangle("triangle", 5, 6, 3)
    assert triangle.name == "triangle"
    assert triangle.site_a == 5
    assert triangle.site_b == 6
    assert triangle.site_c == 3

    assert triangle.area == (7 * (7 - 5) * (7 - 6) * (7 - 3)) ** 0.5

    assert circle.area + triangle.area == circle.add_area(triangle)


def test_add_area_circle_and_rentangle():
    circle = Circle("circle", 5)
    assert circle.name == "circle"
    assert circle.radius == 5
    assert circle.area == 5 * 5 * pi

    rentangle = Rectangle("rentangle", 6, 2)
    assert rentangle.name == "rentangle"
    assert rentangle.site_a == 6
    assert rentangle.site_b == 2

    assert rentangle.area == 6 * 2

    assert circle.area + rentangle.area == circle.add_area(rentangle)


def test_add_area_circle_and_square():
    circle = Circle("circle", 5)
    assert circle.name == "circle"
    assert circle.radius == 5
    assert circle.area == 5 * 5 * pi

    square = Square("square", 10)
    assert square.name == "square"
    assert square.site == 10

    assert square.area == 10 * 10

    assert circle.area + square.area == circle.add_area(square)
