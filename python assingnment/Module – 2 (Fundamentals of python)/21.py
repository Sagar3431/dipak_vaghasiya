'''
Write a Python function to reverses a string if its length is a multiple of
4.
'''
input_string = input("Enter a string: ")

if len(input_string) % 4 == 0:
    reversed_string = input_string[::-1]
    print("Reversed string:", reversed_string)
else:
    print("String length is not a multiple of 4. No reversal needed.")

