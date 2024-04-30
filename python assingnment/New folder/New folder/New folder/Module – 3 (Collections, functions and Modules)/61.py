'''
Write a Python program to calculate the area of a trapezoid
'''
def trapezoid_area(a, b, h):
    area=((a+b)*h)/2
    return area

a = 5  # Length of the first parallel side (base)  # 5+7=11 12*4=48 48/2 ans = 24
b = 7  # Length of the second parallel side (base)
h = 4  # Height of the trapezoid
area = trapezoid_area(a, b, h)
print("Area of the trapezoid:", area)