superhero = {1, 2, 3, 4}

print(superhero)

def getSquare(num):
    return  num*num

result = map(getSquare, superhero)

resultTwo = set(result)

print(resultTwo)


# py11 class 03 - all() or any() operator are used to as AND & OR gate
# all() - AND : if any value is 0 or None - its FALSE
# any() - OR : if any value is 0 or None and any value in non-zero its TRUE
