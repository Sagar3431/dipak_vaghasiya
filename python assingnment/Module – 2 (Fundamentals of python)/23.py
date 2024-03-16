'''
Write a Python function to insert a string in the middle of a string.
'''

# Prompt the user to enter the original string and store it in the variable original_string
original_string = input("Enter the original string: ")

# Prompt the user to enter the string to insert and store it in the variable string_to_insert
string_to_insert = input("Enter the string to insert: ")

# Calculate the index at which to insert the string by dividing the length of the original string by 2
insert_index = len(original_string) // 2

# Construct the result string by inserting the string to insert at the calculated index
result_string = original_string[:insert_index] + string_to_insert + original_string[insert_index:]

# Print the result string
print("Result:", result_string)

