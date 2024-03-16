'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
'''

# Prompt the user to enter the first string and store it in the variable string1
string1 = input("Enter the first string: ")

# Prompt the user to enter the second string and store it in the variable string2
string2 = input("Enter the second string: ")

# Check if both strings have at least two characters
if len(string1) >= 2 and len(string2) >= 2:
    # Swap the first two characters of string1 with the first two characters of string2
    swapped_str1 = string2[:2] + string1[2:]
    
    # Swap the first two characters of string2 with the first two characters of string1
    swapped_str2 = string1[:2] + string2[2:]
    
    # Print the two swapped strings separated by a space
    print(swapped_str1 + ' ' + swapped_str2)
else:
    # If any of the strings has less than two characters, print a message
    print("Both strings should have at least two characters")




