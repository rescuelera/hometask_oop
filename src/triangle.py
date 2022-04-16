from src.figure import Figure


class Triangle(Figure):
    def __init__(self, name, site_a, site_b, site_c):
        if site_a < 0 or site_b < 0 or site_c < 0:
            raise ValueError("Site must be greather than 0")
        self.name = name
        self.site_a = site_a
        self.site_b = site_b
        self.site_c = site_c

    @property
    def area(self):
        polyperimetr = self.perimeter / 2
        return (polyperimetr * (polyperimetr - self.site_a) * (polyperimetr - self.site_b) * (
                    polyperimetr - self.site_c)) ** 0.5

    @property
    def perimeter(self):
        return self.site_a + self.site_b + self.site_c
