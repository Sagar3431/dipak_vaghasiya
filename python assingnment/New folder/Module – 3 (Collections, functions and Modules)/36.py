'''
How Do You Check The Presence Of A Key In A Dictionary?
'''

# 1 Using the in operator:
# Dictionary to check
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Key to check for existence
key_to_check = 'b'

# Check if the key exists in the dictionary using the 'in' operator
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
# 2 Using the get() method:
# Key to check for existence
key_to_check = 'b'

# Check if the key exists in the dictionary using the 'get()' method
if my_dict.get(key_to_check) is not None:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")