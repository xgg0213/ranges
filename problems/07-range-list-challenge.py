# Create a function that returns a list of 100 randomly generated numbers.

import random
# Write your function here.
def rng(input):
    return random.randint(1, 101)

print(rng([]))