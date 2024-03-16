# def sum_of_positive_integers(n):
#     if n <= 0:
#         return "Please enter a positive integer."
#     else:
#         total = 0
#         for i in range(1, n + 1):
#             total += i
#         return total

# # Example usage:
# n = int(input("Enter a positive integer n: "))
# result = sum_of_positive_integers(n)
# print("The sum of the first", n, "positive integers is:", result)


'''
Write a python program to sum of the first n positive integers.
'''
# Taking input from the user for a number
num1 = int(input("Enter Your Num: "))

# Checking if the number is less than or equal to zero
if num1 <= 0:
    print("Please enter a positive integer.")
else:
    # If the number is positive, initialize a variable to store the total sum
    total = 0
    
    # Iterate through positive integers up to the given number and calculate their sum
    for i in range(1, num1 + 1):
        total += i  # Adding each positive integer to the total
    
    # Printing the sum of the first 'num1' positive integers
    print("The sum of the first", num1, "positive integers is:", total)


     
    

