'''
Write a Python program to test whether a passed letter is a vowel or not.
'''

def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter = letter.lower()
    if letter in vowels:
        return True
    else:
        return False

input_letter = input("Enter a letter: ")

if len(input_letter) == 1 and input_letter.isalpha():
    if is_vowel(input_letter):
        print(input_letter, "is a vowel.")
    else:
        print(input_letter, "is not a vowel.")
else:
    print("Please enter a single letter.")
