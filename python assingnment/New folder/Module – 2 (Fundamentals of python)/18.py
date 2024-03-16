'''
Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.
'''

# Prompt the user to enter a string and store it in the variable given_string
given_string = input("Enter a string: ")

# Check if the length of the given string is at least 3
if len(given_string) >= 3:
    # Check if the last three characters of the string are 'ing'
    if given_string[-3:] == 'ing':
        # If the condition is true, append 'ly' to the string
        result = given_string + 'ly'
    else:
        # If the condition is false, append 'ing' to the string
        result = given_string + 'ing'
else:
    # If the length of the string is less than 3, leave it unchanged
    result = given_string

# Print the result
print("Result:", result)

