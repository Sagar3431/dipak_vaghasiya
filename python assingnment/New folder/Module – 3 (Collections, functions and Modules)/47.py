'''
Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})

'''

from collections import Counter


list_of_dicts = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

# Initialize a Counter to combine values
combined_counter = Counter()

# Iterate over each dictionary in the list
for dictionary in list_of_dicts:
    # Update the Counter with the amount for each item
    combined_counter[dictionary['item']] += dictionary['amount']

# Print the combined Counter
print("Combined Counter:")
print(combined_counter)
