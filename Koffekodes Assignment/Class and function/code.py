#Create a base class Shape with methods to calculate area and perimeter.
# Derive classes Circle and Rectangle from it and override the methods.

# from abc import ABC,abstractmethod
# from math import pi

# #AbstractMethod
# class Shape():
#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return pi * (self.radius ** 2)

#     def calculate_perimeter(self):
#         return 2 * pi * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)

# circle = Circle(5)
# print(f"Circle area: {circle.calculate_area()}, perimeter: {circle.calculate_perimeter()}")

# rectangle = Rectangle(4, 6)
# print(f"Rectangle area: {rectangle.calculate_area()}, perimeter: {rectangle.calculate_perimeter()}")


# -	Create a Calculator class with multiple methods for addition, subtraction, multiplication, and division. Implement method overloading 
# to handle different parameter types (int, float, and possibly more). Demonstrate the usage of these overloaded methods.

# class Calculator:
#     def addition(self, a, b=0):
#         return a + b

#     def multiply(self, a, b=1):
#         return a * b

#     def subtraction(self, a, b=0):
#         return a - b

#     def divide(self, a, b=1):
#         if b != 0:
#             return a / b
#         print ('Can not divide by zero')


# calculator = Calculator()
# print(calculator.addition(10))
# print(calculator.subtraction(50, 20))
# print(calculator.multiply(10, 20))
# print(calculator.divide(100, 20))


# -	Implement a base class Shape with methods for calculating area and perimeter. 
#   Create derived classes such as Circle, Rectangle, and Triangle that inherit from Shape and override the relevant methods. 
# 	Demonstrate polymorphism by creating instances of these classes and calling the area and perimeter methods.

# from abc import ABC,abstractmethod
# from math import pi

# #AbstractMethod
# class Shape():
#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return pi * (self.radius ** 2)

#     def calculate_perimeter(self):
#         return 2 * pi * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)

# circle = Circle(5)
# print(f"Circle area: {circle.calculate_area()}, perimeter: {circle.calculate_perimeter()}")

# rectangle = Rectangle(4, 6)
# print(f"Rectangle area: {rectangle.calculate_area()}, perimeter: {rectangle.calculate_perimeter()}")
