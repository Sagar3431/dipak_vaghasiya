'''
Write a Python program to map two lists into a dictionary
'''
# Two lists to map into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Create a dictionary by mapping keys and values
mapped_dict = dict(zip(keys, values))

# Print the resulting dictionary
print("Mapped Dictionary:", mapped_dict)
