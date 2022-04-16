import pytest

from src.square import Square


def test_square_check_general_case():
    square1 = Square("square1", 5, )
    assert square1.name == "square1"
    assert square1.site == 5
    assert square1.area == 5 * 5


def test_square_zero_site():
    square_site_0 = Square("square_site_a_0", 0)
    assert square_site_0.area == 0
    assert square_site_0.perimeter == 0


def test_square_negative_site_a():
    with pytest.raises(ValueError):
        Square("site-1", -1)


def test_rentangle_summa_areas():
    square1 = Square("square1", 5)
    assert square1.name == "square1"
    assert square1.site == 5

    assert square1.area == 5 * 5

    square2 = Square("square2", 10)
    assert square2.name == "square2"
    assert square2.site == 10

    assert square1.area == 10 * 10

    assert square1.area + square2.area == square1.add_area(square2)
