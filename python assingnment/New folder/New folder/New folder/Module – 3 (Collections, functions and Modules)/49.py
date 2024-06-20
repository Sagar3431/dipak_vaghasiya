'''
Write a Python function to calculate the factorial of a number (a
nonnegative integer)
'''

# number = int(input("Enter a non-negative integer: "))

# # Check if the number is non-negative
# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# elif number == 0 or number == 1:
#     print("Factorial of", number, "is 1")
# else:
#     factorial = 1
#     # Calculate factorial
#     for i in range(2, number + 1):
#         factorial *= i
#     print("Factorial of", number, "is", factorial)

import math

num=int(input("num : "))
factorial=math.factorial(num)
print(f"factorial {num} is {factorial}")
