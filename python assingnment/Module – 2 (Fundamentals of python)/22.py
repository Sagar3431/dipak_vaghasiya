'''
Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.
'''
# Prompt the user to enter a string and store it in the variable input_string
input_string = input("Enter a string: ")

# Check if the length of the input string is less than 2
if len(input_string) < 2:
    # If the length is less than 2, assign an empty string to the result
    result = ""  
else:
    # If the length is 2 or greater, concatenate the first two characters
    # with the last two characters of the input string
    result = input_string[:2] + input_string[-2:]

# Print the result
print("Result:", result)

