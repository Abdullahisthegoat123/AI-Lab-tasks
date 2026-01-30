import math
from abc import ABC, abstractmethod

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Line(Shape):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def perimeter(self):
        return math.dist((self.p1.x, self.p1.y), (self.p2.x, self.p2.y))

    def draw(self):
        print(f"Line from {self.p1} to {self.p2}")


class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def area(self):
        x1, y1 = self.points[0].x, self.points[0].y
        x2, y2 = self.points[1].x, self.points[1].y
        x3, y3 = self.points[2].x, self.points[2].y
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    def perimeter(self):
        return (
            math.dist((self.points[0].x, self.points[0].y), (self.points[1].x, self.points[1].y)) +
            math.dist((self.points[1].x, self.points[1].y), (self.points[2].x, self.points[2].y)) +
            math.dist((self.points[2].x, self.points[2].y), (self.points[0].x, self.points[0].y))
        )

    def draw(self):
        print("Triangle at points:", ", ".join(str(p) for p in self.points))


class Rectangle(Shape):
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f"Rectangle at {self.top_left}, width={self.width}, height={self.height}")


class Square(Rectangle):
    def __init__(self, top_left, side):
        super().__init__(top_left, side, side)

    def draw(self):
        print(f"Square at {self.top_left}, side={self.width}")


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self):
        print(f"Circle at center {self.center}, radius={self.radius}")


class Pentagon(Shape):
    def __init__(self, points):
        self.points = points

    def area(self):
        side = math.dist(
            (self.points[0].x, self.points[0].y),
            (self.points[1].x, self.points[1].y)
        )
        return (5 * side * side) / (4 * math.tan(math.pi / 5))

    def perimeter(self):
        return sum(
            math.dist(
                (self.points[i].x, self.points[i].y),
                (self.points[(i+1) % 5].x, self.points[(i+1) % 5].y)
            )
            for i in range(5)
        )

    def draw(self):
        print("Pentagon at points:", ", ".join(str(p) for p in self.points))


class Quadrilateral(Shape):
    def __init__(self, points):
        self.points = points

    def area(self):
        t1 = Triangle(self.points[0], self.points[1], self.points[2])
        t2 = Triangle(self.points[0], self.points[2], self.points[3])
        return t1.area() + t2.area()

    def perimeter(self):
        return sum(
            math.dist(
                (self.points[i].x, self.points[i].y),
                (self.points[(i+1) % 4].x, self.points[(i+1) % 4].y)
            )
            for i in range(4)
        )

    def draw(self):
        print("Quadrilateral at points:", ", ".join(str(p) for p in self.points))


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(5, 2)
    p4 = Point(1, 6)
    p5 = Point(2, 4)

    shapes = [
        Line(p1, p2),
        Triangle(p1, p2, p3),
        Rectangle(p1, 4, 3),
        Square(p1, 4),
        Circle(p1, 5),
        Pentagon([p1, p2, p3, p5, p4]),
        Quadrilateral([p1, p2, p3, p4])
    ]

    for shape in shapes:
        shape.draw()
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())
        print("-" * 30)