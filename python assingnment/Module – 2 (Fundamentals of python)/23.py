'''
Write a Python function to insert a string in the middle of a string.
'''

original_string = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

insert_index = len(original_string) // 2

result_string = original_string[:insert_index] + string_to_insert + original_string[insert_index:]

print("Result:", result_string)
