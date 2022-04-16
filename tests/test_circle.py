from math import pi

import pytest

from src.circle import Circle


def test_circle_check_general_case():
    circle1 = Circle("circle1", 10)
    assert circle1.name == "circle1"
    assert circle1.radius == 10
    assert circle1.area == 10 * 10 * pi


def test_circle_zero_radius():
    circle_radius_0 = Circle("circle_radius0", 0)
    assert circle_radius_0.area == 0
    assert circle_radius_0.perimeter == 0


def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle("circle_radius-1", -1)


def test_circle_summa_areas():
    circle1 = Circle("circle1", 5)
    assert circle1.name == "circle1"
    assert circle1.radius == 5
    assert circle1.area == 5 * 5 * pi

    circle2 = Circle("circle2", 10)
    assert circle2.name == "circle2"
    assert circle2.radius == 10
    assert circle2.area == 10 * 10 * pi

    assert circle1.area + circle2.area == circle1.add_area(circle2)
