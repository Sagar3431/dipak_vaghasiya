'''
Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers.
'''
def find_max_min(numbers):
     if not numbers:
        return None, None

     max_num = max(numbers)
     min_num = min(numbers)
     return max_num, min_num
 
decimal_numbers = [3.14, 2.718, 1.618, 0.577, 2.302]
max_num, min_num = find_max_min(decimal_numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)