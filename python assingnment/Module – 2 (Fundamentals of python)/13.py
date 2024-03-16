'''
Write a Python program to count the number of characters (character frequency) in a string

'''

# Define an empty dictionary to store character frequencies
frequency_dict = {}

# Prompt the user to enter a string and store it in the variable user_input
user_input = input("Enter a string: ")

# Iterate through each character in the input string
for char in user_input:
    # Increment the frequency count for the current character in the dictionary
    # If the character is not in the dictionary, initialize its count to 1
    frequency_dict[char] = frequency_dict.get(char, 0) + 1

# Print the character frequencies
print("Character frequency:")
for char, frequency in frequency_dict.items():
    print(f"'{char}': {frequency}")

