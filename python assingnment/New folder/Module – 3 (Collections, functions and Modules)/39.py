'''
Write a Python script to merge two Python dictionaries
'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Merge dict2 into dict1 using the update() method
dict1.update(dict2)
# Print the merged dictionary
print(dict1)