from math import pi

from src.figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        if radius < 0:
            raise ValueError("Radius must be greather than 0")
        self.name = name

        self.radius = radius

    @property
    def area(self):
        return self.radius * self.radius * pi

    @property
    def perimeter(self):
        return self.radius * 2 * pi
