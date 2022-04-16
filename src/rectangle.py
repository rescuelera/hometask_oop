from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, name, site_a, site_b):
        if site_a < 0 or site_b < 0:
            raise ValueError("Site must be greather than 0")

        self.name = name
        self.site_a = site_a
        self.site_b = site_b

    @property
    def area(self):
        return self.site_a * self.site_b

    @property
    def perimeter(self):
        return self.site_a * 2 + self.site_b * 2
