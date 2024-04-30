'''
Write a Python program to print all unique values in a dictionary.
'''
example_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Create an empty set to store unique values
unique_value=set()
# Iterate over the values in the dictionary
for value in example_dict.values():
    unique_value.add(value)
    
print("Unique values in the dictionary:", unique_value)
