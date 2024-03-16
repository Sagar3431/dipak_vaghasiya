'''
Write python program that swap two number with temp variable and without temp variable.
'''
# Swapping with a temporary variable
# Swapping two variables using a temporary variable
num1 = 5
num2 = 10

# Printing the values before swapping
print("Before swapping:", num1, num2)

# Using a temporary variable to swap values
temp = num1
num1 = num2
num2 = temp

# Printing the values after swapping
print("After swapping:", num1, num2)


# Swapping two variables without using a temporary variable
num1 = 5
num2 = 10

# Printing the values before swapping
print("Before swapping:", num1, num2)

# Swapping without a temporary variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Printing the values after swapping
print("After swapping:", num1, num2)

