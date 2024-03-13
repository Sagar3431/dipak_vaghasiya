'''
Write python program that swap two number with temp variable and without temp variable.
'''
# Swapping with a temporary variable
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

num1 = 5
num2 = 10
print("Before swapping:", num1, num2)
num1, num2 = swap_with_temp(num1, num2)
print("After swapping:", num1, num2)


def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1 = 5
num2 = 10
print("Before swapping:", num1, num2)
num1, num2 = swap_without_temp(num1, num2)
print("After swapping:", num1, num2)

