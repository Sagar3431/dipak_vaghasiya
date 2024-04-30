'''
Write a Python program to calculate the area of a parallelogram
'''
def parallelogram_area(base, height):
    area=base*height
    return area

base = 8  # Length of the base of the parallelogram  8*5=40 ans is a 40
height = 5  # Height of the parallelogram
area = parallelogram_area(base, height)
print("Area of the parallelogram:", area)