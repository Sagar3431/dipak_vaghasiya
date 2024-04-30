'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd

'''
from itertools import product

# Sample data
data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Get all combinations of letters
combinations = list(product(*data.values()))

# Join the letters in each combination and print
for combination in combinations:
    print(''.join(combination), end=' ')
