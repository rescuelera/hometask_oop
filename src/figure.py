class Figure:
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("This is not a figure")
        return self.area + other_figure.area

    @property
    def area(self):
        raise NotImplemented()

    @property
    def perimeter(self):
        raise NotImplemented()
