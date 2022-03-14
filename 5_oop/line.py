import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def distance(self):
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    def slope(self):
        return (point2.y - point1.y) / (point2.x - point1.x)


if __name__ == '__main__':
    point1 = Point(3, 2)
    point2 = Point(8, 10)

    my_line = Line(point1, point2)

    print(my_line.distance())
    print(my_line.slope())
