'''
Write a Python program to calculate surface volume and area of a
cylinder
'''
import math

def cylinder_surface_area(radius, height):
    area=2*math.pi*radius*(radius+height)
    return area
def cylinder_volume(radius, height):
    valume=math.pi*radius**2*height
    return valume
def cylinder_lateral_surface_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    return lateral_area

radius = 5
height = 10

surface_area = cylinder_surface_area(radius, height)
print("Surface Area of Cylinder:", surface_area)

volume = cylinder_volume(radius, height)
print("Volume of Cylinder:", volume)

lateral_surface_area = cylinder_lateral_surface_area(radius, height)
print("Lateral Surface Area of Cylinder:", lateral_surface_area)