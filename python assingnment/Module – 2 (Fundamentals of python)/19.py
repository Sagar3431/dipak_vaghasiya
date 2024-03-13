'''
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

given_string = input("Enter a string: ")

index_not = given_string.find('not')
index_poor = given_string.find('poor')


if index_not != -1 and index_poor != -1 and index_not < index_poor:
    result = given_string[:index_not] + 'good' + given_string[index_poor + 4:]
else:
    result = given_string

print("Result:", result)
