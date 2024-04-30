'''
Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}).

'''


# Two dictionaries to combine
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries by adding values for common keys
combined_dict = {}
for key in d1.keys() | d2.keys():
    combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)
