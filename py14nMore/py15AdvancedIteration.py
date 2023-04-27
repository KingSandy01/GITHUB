# itertools - Functions creating iterators for efficient looping
# three types 1. Infinite Iterator 2. Terminating Iterators 3. Combinatory Iterators

import itertools

# myHeros = ["Superman", "Batman", "Deadpool"]
# myloopy = itertools.cycle(myHeros)
# print(myloopy)
# print(next(myloopy))

# OUTPUT:
# Superman

# -------------------------------------

# myNums = [1, 2, 3, 4, 5]
# myacc = itertools.accumulate(myNums)
# print(list(myacc))
# myNums = [1, 2, 3, 4, 5, 5, 3, 4, 3]
# myacc = itertools.accumulate(myNums, max)
# print(list(myacc))

# OUTPUT: 
# [1, 3, 6, 10, 15]
# [1, 2, 3, 4, 5, 5, 5, 5, 5]

# -----------------------------------------------

inter = itertools.chain("Sandeep", "Satapathy")
print(list(inter))

#OUTPUT:
# ['S', 'a', 'n', 'd', 'e', 'e', 'p', 'S', 'a', 't', 'a', 'p', 'a', 't', 'h', 'y']