'''
Write a Python program to find the highest 3 values in a dictionary
'''
# Dictionary
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40, 'e': 25}

# Sorting dictionary items by values in descending order
sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# Getting the keys of the highest three values
highest_three_keys = [item[0] for item in sorted_items[:3]]

# Output
print("Highest three values:", highest_three_keys)
