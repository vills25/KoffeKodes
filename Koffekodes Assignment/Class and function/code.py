#Create a base class Shape with methods to calculate area and perimeter.
# Derive classes Circle and Rectangle from it and override the methods.

from abc import ABC,abstractmethod
from math import pi

#AbstractMethod
class Shape():
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(5)
print(f"Circle area: {circle.calculate_area()}, perimeter: {circle.calculate_perimeter()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.calculate_area()}, perimeter: {rectangle.calculate_perimeter()}")