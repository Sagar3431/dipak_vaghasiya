'''
Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.
'''

given_string = input("Enter a string: ")

if len(given_string) >= 3:
    if given_string[-3:] == 'ing':
        result = given_string + 'ly'
    else:
        result = given_string + 'ing'
else:
    result = given_string

print("Result:", result)
