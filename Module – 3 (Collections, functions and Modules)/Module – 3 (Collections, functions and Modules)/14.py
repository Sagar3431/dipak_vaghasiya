'''
Write a Python program to find the second smallest number in a list.
'''

# Define a list of numbers
numbers = [10, 10, 8, 3, 9, 7]

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# The second smallest number is the second element of the sorted list
second_smallest = sorted_numbers[1]

# Print the second smallest number
print("Second smallest number:", second_smallest)
