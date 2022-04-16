from src.figure import Figure


class Square(Figure):
    def __init__(self, name, site):
        if site < 0:
            raise ValueError("Site must be greather than 0")
        self.name = name
        self.site = site

    @property
    def area(self):
        return self.site * 2

    @property
    def perimeter(self):
        return self.site * 4
