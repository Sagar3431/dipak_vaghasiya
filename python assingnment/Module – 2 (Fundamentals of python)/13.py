'''
Write a Python program to count the number of characters (character frequency) in a string

'''

def count_character_frequency(input_string):
    frequency_dict = {}

    # Iterate through each character in the string
    for char in input_string:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict

user_input = input("Enter a string: ")
character_frequency = count_character_frequency(user_input)

print("Character frequency:")
for char, frequency in character_frequency.items():
    print(f"'{char}': {frequency}")
