'''
Write a Python program to test whether a passed letter is a vowel or not.
'''

# Defining a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Taking input from the user
input_letter = input("Enter a letter: ")

# Checking if the input is a single letter and is alphabetic
if len(input_letter) == 1 and input_letter.isalpha():
    # Converting the input letter to lowercase
    input_letter = input_letter.lower()
    
    # Checking if the input letter is a vowel by checking if it exists in the list of vowels
    if input_letter in vowels:
        print(input_letter, "is a vowel.")
    else:
        print(input_letter, "is not a vowel.")
else:
    print("Please enter a single letter.")

