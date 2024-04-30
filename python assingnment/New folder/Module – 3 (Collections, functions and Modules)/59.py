'''
Write a Python program to read a random line from a file.
'''

import random

filename = 'sagar.txt'  # Replace 'your_file.txt' with the path to your file

# Count the total number of lines in the file
with open(filename, 'r') as file:
    total_lines = sum(1 for line in file)

# Generate a random line number
random_line_number = random.randint(1, total_lines)

# Read the random line from the file
with open(filename, 'r') as file:
    for line_number, line in enumerate(file, 1):
        if line_number == random_line_number:
            random_line = line.rstrip()  # Remove newline character if present
            break

print("Random line from the file:", random_line)
