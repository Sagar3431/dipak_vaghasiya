'''
Write a Python function to get the largest number, smallest num and sum
of all from a list.

'''

def get_stats(numbers):
    if not numbers:
        return None, None, 0  # Return None for largest and smallest if list is empty
    
    # Initialize variables to store largest and smallest numbers
    largest = numbers[0]
    smallest = numbers[0]
    
    # Initialize variable to store sum of all numbers
    total_sum = 0
    
    # Iterate through the list to find the largest, smallest, and sum of all numbers
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total_sum += num
    
    return largest, smallest, total_sum

# Example usage:
numbers = [2, 10, 5, 20, 1]
largest, smallest, total_sum = get_stats(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total_sum)
