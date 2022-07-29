from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def area(self):
        return 5 * 15

    def perimeter(self):
        return self.side * self.h * 2


t = Triangle(2,7)
print(t.area())
