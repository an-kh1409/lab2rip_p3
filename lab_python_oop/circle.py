from math import pi
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor


class Circle(GeometricFigure):
    def __init__(self, r, c):
        self.radius = r
        self.color = FigureColor(c)
        self.type = "Circle"

    def get_type(self):
        return self.type

    def area(self):
        return round(self.radius * self.radius * pi, 5)

    def __repr__(self):
        return '{} with radius {} and color {}, which has area {}'.format(self.get_type(), self.radius,
                                                                          self.color, self.area())
