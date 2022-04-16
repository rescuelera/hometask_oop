from math import pi

import pytest

from src.rectangle import Rectangle


def test_rentangle_check_general_case():
    rentangle1 = Rectangle("rentangle1", 5, 10)
    assert rentangle1.name == "rentangle1"
    assert rentangle1.site_a == 5
    assert rentangle1.site_b == 10
    assert rentangle1.area == 5 * 10


def test_rentangle_zero_site_a():
    rentangle_site_0 = Rectangle("rentangle_site_a_0", 0, 5)
    assert rentangle_site_0.area == 0
    assert rentangle_site_0.perimeter == 10


def test_rentangle_zero_site_b():
    rentangle_site_0 = Rectangle("rentangle_site_b_0", 5, 0)
    assert rentangle_site_0.area == 0
    assert rentangle_site_0.perimeter == 10


def test_rentangle_negative_site_a():
    with pytest.raises(ValueError):
        Rectangle("site_a-1", -1, 5)


def test_rentangle_negative_site_b():
    with pytest.raises(ValueError):
        Rectangle("site_b-1", 1, -1)


def test_rentangle_summa_areas():
    rentangle1 = Rectangle("rentangle1", 5, 6)
    assert rentangle1.name == "rentangle1"
    assert rentangle1.site_a == 5
    assert rentangle1.site_b == 6

    assert rentangle1.area == 5 * 6

    rentangle2 = Rectangle("rentangle2", 6, 2)
    assert rentangle2.name == "rentangle2"
    assert rentangle2.site_a == 6
    assert rentangle2.site_b == 2

    assert rentangle2.area == 6 * 2

    assert rentangle1.area + rentangle2.area == rentangle1.add_area(rentangle2)
