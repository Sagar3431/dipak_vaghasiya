'''
How can you pick a random item from a range?
ans: To pick a random item from a range in Python,  convert the range to a list and then use the random.choice() function.
'''
import random

my_range=range(1,11)
random_items=random.choice(list(my_range))
print(random_items)