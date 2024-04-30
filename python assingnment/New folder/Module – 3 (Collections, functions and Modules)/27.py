'''
Write a Python program to find the repeated items of a tuple.
'''

# Tuple to find repeated items from
my_tuple = (1, 2, 3, 4, 2, 3, 5, 6, 5, 7)

# Create an empty dictionary to store item counts
item_counts = {}

# Iterate through the tuple and count occurrences of each item
for item in my_tuple:
    if item in item_counts:
        item_counts[item] += 1
    else:
        item_counts[item] = 1

# Find repeated items
repeated_items = [item for item, count in item_counts.items() if count > 1]

# Print the repeated items
print("Repeated Items:", repeated_items)
