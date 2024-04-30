'''
Write a Python program to remove duplicates from a list.
'''

# Original list with duplicates
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# Removing duplicates by converting the list to a set and back to a list
unique_list = list(set(my_list))

# Printing the unique list
print("Original list with duplicates:", my_list)
print("List after removing duplicates:", unique_list)
