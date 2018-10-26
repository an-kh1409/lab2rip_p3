from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, s, c):
        super().__init__(s, s, c)
        self.type = "Square"

    def get_type(self):
        return self.type

    def __repr__(self):
        return '{} with side {} and color {}, which has area {}'.format(self.get_type(), self.height,
                                                                        self.color, self.area())
