'''
Write a Python program to returns sum of all divisors of a number
'''
def sum_of_divisors(n):
    divisor_sum = 0
    for i in range(1, int(n**0.5) + 1):
        # If i is a divisor of n
        if n % i == 0:
            divisor_sum += i
            # If i is not the square root of n, add the corresponding divisor
            if n // i != i:
                divisor_sum += n // i
    return divisor_sum
number = 12
print("Sum of divisors of", number, ":", sum_of_divisors(number))
    