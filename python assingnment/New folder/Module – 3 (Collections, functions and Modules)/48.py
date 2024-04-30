'''
Write a Python program to create a dictionary from a string.
'''

input_string = 'w3resource'

# Initialize an empty dictionary to store character counts
char_count = {}

# Iterate over each character in the string
for char in input_string:
    # Increment the count for the current character
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the resulting dictionary
print("Dictionary from string:")
print(char_count)
