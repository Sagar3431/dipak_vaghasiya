'''
How will you set the starting value in generating random numbers?
'''
import random

# Set the seed value
random.seed(42)

# Generate a random floating-point number between 0.0 and 1.0
random_float = random.random()
print("Random floating-point number:", random_float)

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print("Random integer:", random_int)
