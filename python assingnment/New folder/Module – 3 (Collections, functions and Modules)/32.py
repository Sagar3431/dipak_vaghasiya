'''
Write a Python script to sort (ascending and descending) a dictionary by
value.

'''

# Dictionary to be sorted
my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# Sort the dictionary by value in ascending order
sorted_dict_asc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

# Sort the dictionary by value in descending order
sorted_dict_desc = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}

# Print the sorted dictionaries
print("Sorted Dictionary (Ascending):", sorted_dict_asc)
print("Sorted Dictionary (Descending):", sorted_dict_desc)
