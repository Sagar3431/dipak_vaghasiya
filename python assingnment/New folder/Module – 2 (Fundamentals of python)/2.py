'''
Write a Python program to get the Factorial number of given number.
'''
# Taking input from the user
num = int(input("Enter a number: "))

# Initializing factorial variable
fact = 1

# Checking if the number is negative
if num < 0:
    print("Factorial of a negative number does not exist")

# Checking if the number is 0
if num == 0:
    print("Factorial of 0 is", 1)

# Calculating factorial for positive numbers
if num > 0:
    # Looping through numbers from 1 to the given number
    for i in range(1, num + 1):
        fact = fact * i  # Calculating factorial
        print("The factorial of the given number is", fact)
 