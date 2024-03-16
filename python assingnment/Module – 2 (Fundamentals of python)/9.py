'''
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
'''

# Taking input from the user for three numbers
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
num3 = int(input("Enter Third Num: "))

# Checking if any two numbers are equal
if num1 == num2 or num2 == num3 or num1 == num3:
    print("Two values are equal, sum:", 0)
else:
    # If no two numbers are equal, calculating and printing the sum of all three integers
    print("The sum of three integers is:", num1 + num2 + num3)
