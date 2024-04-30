'''
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
'''
# Given list of strings
string_list = ["abc", "xyz", "aba", "1221", "aa"]

# Initialize a counter variable to keep track of the number of strings meeting the criteria
count = 0

# Iterate through each string in the list
for string in string_list:
    # Check if the length of the string is 2 or more and if the first and last characters are the same
    if len(string) >= 2 and string[0] == string[-1]:
        # If the conditions are met, increment the counter
        count += 1

# Print the result
print("Number of strings where the first and last character are the same:", count)
