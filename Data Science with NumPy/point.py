import math


class Point:
    # write a docstring here for the class!
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        # WRITE ME
        return f"({self.x}, {self.y})"

    def __repr__(self):
        # WRITE ME
        return f"Point({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_from(self, other_pt):
        return math.sqrt((self.x - other_pt.x) ** 2 + (self.y - other_pt.y) ** 2)

    pass


if __name__ == "__main__":
    p1 = Point()
    p2 = Point(3, 4)
    p3 = Point(-3, 4)
    p4 = Point(7, 2)
    p5 = Point(-9, 16)
    points = [p1, p2, p3, p4, p5]
    for pa in points:
        print("---")
        print(pa)
        print(repr(pa))
        for pb in points:
            print(pa.distance_from(pb))
            pass
        pass
    p1.move(1, 1)
    p2.move(-2, 3)
    p3.move(4, -5)
    for pa in points:
        print("---")
        print(pa)
        print(repr(pa))
        for pb in points:
            print(pa.distance_from(pb))
            pass
        pass
    pass
