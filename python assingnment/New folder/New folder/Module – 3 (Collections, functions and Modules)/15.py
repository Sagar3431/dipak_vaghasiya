'''
Write a Python program to get unique values from a list
'''

# Define a list with duplicate values
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Convert the list to a set to get unique values
unique_values_set = set(my_list)

# Convert the set back to a list
unique_values_list = list(unique_values_set)

# Print the unique values
print("Unique values:", unique_values_list)

# my_list=[1,2,3,4,5,6,7,1,2,3,4,5,6,7,8]

# unique_value_set=set(my_list)
# unique_value_list=list(unique_value_set)
# print(unique_value_list)
