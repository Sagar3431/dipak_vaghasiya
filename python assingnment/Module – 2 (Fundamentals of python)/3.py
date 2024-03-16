'''
Write a Python program to get the Fibonacci series of given range.
'''

# Initializing variables for the first two numbers in the Fibonacci sequence
a = 0
b = 1

# Taking input from the user for the number of Fibonacci sequence elements to print
num = int(input("Enter the number of Fibonacci sequence elements to generate: "))

# If the user wants only the first number in the sequence
if num == 1:
    print(a)
else:
    # Printing the first two numbers in the Fibonacci sequence
    print(a)
    print(b)
    
    # Generating the rest of the Fibonacci sequence
    for i in range(2, num):  # Starting from 2 as the first two numbers are already printed
        c = a + b  # Calculating the next Fibonacci number by adding the previous two
        a = b  # Updating 'a' to the second last number
        b = c  # Updating 'b' to the last number
        print(c)  # Printing the next Fibonacci number
