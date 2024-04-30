'''
Write a Python program to convert degree to radian
'''
import math
def degrees_to_radians(degrees):
    radians=degrees*(math.pi/180)
    return radians

degrees = 90
radians = degrees_to_radians(degrees)
print("Degrees:", degrees)
print("Radians:", radians)