# Iterators and Generators

import random

heros = ["batman", "Hulk", "Thor"]

for h in heros:
    print(h)

# print(range(6))

def magic():
    for i in range(6):
        # return random.randint(1, 20) # Iteratable error will come
        yield random.randint(1, 20)

for number in magic():
    print("Value is", number)
