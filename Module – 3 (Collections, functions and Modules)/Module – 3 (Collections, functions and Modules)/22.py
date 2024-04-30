'''
Write a Python program to check whether an element exists within a
tuple.
'''
# Tuple to be checked
my_tuple = (1, 2, 3, 4, 5)

# Element to check
element = 2

# Check if element exists in the tuple
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")
