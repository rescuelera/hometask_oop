import pytest

from src.triangle import Triangle


def test_triangle_check_zero_area():
    triangle1 = Triangle("triangle1", 5, 10, 15)
    assert triangle1.name == "triangle1"
    assert triangle1.site_a == 5
    assert triangle1.site_b == 10
    assert triangle1.site_c == 15
    assert triangle1.area == 0


def test_triangle_zero_site_a():
    triangle_site_a_0 = Triangle("triangle_site_a_0", 0, 5, 5)
    assert triangle_site_a_0.area == 0
    assert triangle_site_a_0.perimeter == 10


def test_triangle_zero_site_b():
    triangle_site_b_0 = Triangle("triangle_site_b_0", 5, 0, 5)
    assert triangle_site_b_0.area == 0
    assert triangle_site_b_0.perimeter == 10


def test_triangle_zero_site_c():
    triangle_site_c_0 = Triangle("triangle_site_c_0", 5, 5, 0)
    assert triangle_site_c_0.area == 0
    assert triangle_site_c_0.perimeter == 10


def test_triangle_zero_site_all():
    triangle_all_sites_0 = Triangle("triangle_all_sites_0", 0, 0, 0)
    assert triangle_all_sites_0.area == 0
    assert triangle_all_sites_0.perimeter == 0


def test_triangle_negative_site_a():
    with pytest.raises(ValueError):
        Triangle("site_a-1", -1, 5, 20)


def test_triangle_negative_site_b():
    with pytest.raises(ValueError):
        Triangle("site_b-1", 1, -5, 20)


def test_triangle_negative_site_c():
    with pytest.raises(ValueError):
        Triangle("site_c-1", 1, 5, -20)


def test_triangle_summa_areas():
    triangle1 = Triangle("triangle1", 5, 6, 3)
    assert triangle1.name == "triangle1"
    assert triangle1.site_a == 5
    assert triangle1.site_b == 6
    assert triangle1.site_c == 3

    assert triangle1.area == (7 * (7 - 5) * (7 - 6) * (7 - 3)) ** 0.5

    triangle2 = Triangle("triangle2", 10, 12, 6)
    assert triangle2.name == "triangle2"
    assert triangle2.site_a == 10
    assert triangle2.site_b == 12
    assert triangle2.site_c == 6

    assert triangle2.area == (14 * (14 - 10) * (14 - 12) * (14 - 6)) ** 0.5

    assert triangle1.area + triangle2.area == triangle1.add_area(triangle2)
