""" 
Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print(circle.area())      # Output: 78.53981633974483
print(circle.perimeter()) # Output: 31.41592653589793
