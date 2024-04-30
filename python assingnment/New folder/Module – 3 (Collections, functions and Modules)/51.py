'''
Write a Python function to check whether a number is perfect or not.
'''
def is_perfect_number(number):
  
    if number <= 0:
        return False

    # Find the sum of proper divisors
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    # Check if the sum of proper divisors equals the number
    return divisor_sum == number

# Test the function
number_to_check = 28
if is_perfect_number(number_to_check):
    print(number_to_check, "is a perfect number")
else:
    print(number_to_check, "is not a perfect number")
