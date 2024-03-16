'''
Write a Python program to check if a number is positive, negative or zero.
'''

# Taking input from the user
num = int(input("Enter Your Number: "))

# Checking if the number is positive
if num > 0:
    print("Number Is Positive")

# Checking if the number is negative
elif num < 0:
    print("Number Is Negative")

# If the number is neither positive nor negative, it must be zero
else:
    print("Zero")
