'''
Write a Python program to check multiple keys exists in a dictionary
'''
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Keys to check for existence
keys_to_check = ['a', 'c', 'e']
# Find the intersection of keys in the dictionary and keys to check
intersection_keys = set(my_dict.keys()) or set(keys_to_check)
# Check if the intersection keys are equal to keys to check
if intersection_keys == set(keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("At least one key does not exist in the dictionary.")