'''
Write a Python function to reverses a string if its length is a multiple of
4.
'''
# Prompt the user to enter a string and store it in the variable input_string
input_string = input("Enter a string: ")

# Check if the length of the input string is divisible by 4
if len(input_string) % 4 == 0:
    # If the length is divisible by 4, reverse the string
    reversed_string = input_string[::-1]
    print("Reversed string:", reversed_string)
else:
    # If the length is not divisible by 4, inform the user that no reversal is needed
    print("String length is not a multiple of 4. No reversal needed.")


