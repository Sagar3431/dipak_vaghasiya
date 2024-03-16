'''
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

# Prompt the user to enter a string and store it in the variable given_string
given_string = input("Enter a string: ")

# Find the index of the substring 'not' in the given string
index_not = given_string.find('not')

# Find the index of the substring 'poor' in the given string
index_poor = given_string.find('poor')

# Check if both 'not' and 'poor' substrings are present in the given string
# and 'not' occurs before 'poor'
if index_not != -1 and index_poor != -1 and index_not < index_poor:
    # Replace the substring between 'not' and 'poor' with 'good'
    result = given_string[:index_not] + 'good' + given_string[index_poor + 4:]
else:
    # If either 'not' or 'poor' is not present or 'not' occurs after 'poor',
    # leave the string unchanged
    result = given_string

# Print the result
print("Result:", result)

