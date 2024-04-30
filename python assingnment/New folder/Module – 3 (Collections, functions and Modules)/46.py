'''
Write a Python program to combine values in python list of dictionaries.
'''

list_of_dicts = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 4, 'b': 5, 'd': 6},
    {'b': 7, 'c': 8, 'e': 9}
]

# Initialize an empty dictionary to store combined values
combined_dict = {}

# Iterate over each dictionary in the list
for dictionary in list_of_dicts:
    # Iterate over key-value pairs in the dictionary
    for key, value in dictionary.items():
        # Update the combined dictionary
        combined_dict[key] = combined_dict.get(key, 0) + value

# Print the combined dictionary
print("Combined dictionary:")
print(combined_dict)
