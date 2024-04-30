'''
Write a Python function to check whether a number is in a given range
'''
def in_range(number, start, end):
    return start <= number <= end

# Example usage:
number = 7
start = 1
end = 10
print(in_range(number, start, end))  # Output will be True
