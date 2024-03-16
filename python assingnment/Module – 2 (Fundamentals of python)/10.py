'''
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

# Taking input from the user for two numbers
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))

# Checking if any of the following conditions are met:
# 1. If the two numbers are equal
# 2. If the absolute difference between the two numbers is 5
# 3. If the sum of the two numbers is 5
if num1 == num2 or abs(num1 - num2) == 5 or num1 + num2 == 5:
    print("true")
else:
    print("false")
