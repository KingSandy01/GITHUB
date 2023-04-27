

heroes = list()

while True:
    getInput = input("Enter a Super-Hero: ")
    if getInput == "q":
        break
    heroes.append(getInput)

print(heroes)