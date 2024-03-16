'''
Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user
'''

# Taking input from the user
num1 = int(input("Enter Your Number: "))

# Checking if the number is even or odd
if num1 % 2 == 0:  # If the remainder when divided by 2 is 0, it's even
    print("Number Is Even")
else:
    print("Number Is Odd")
