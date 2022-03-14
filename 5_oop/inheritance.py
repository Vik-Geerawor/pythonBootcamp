class Shape:
    def __init__(self, name):
        self.name = name


class Circle(Shape):
    # class var
    pi = 3.14

    def __init__(self, radius):
        Shape.__init__(self, 'Circle')
        self.radius = radius

    def perimeter(self):
        return 2 * Circle.pi * self.radius

    def area(self):
        return Circle.pi * self.radius ** 2


if __name__ == '__main__':
    c1 = Circle(2)
    print(f"Name: {c1.name}")
    print(f"Perimeter: {c1.perimeter()}")
    print(f"Area: {c1.area()}")
