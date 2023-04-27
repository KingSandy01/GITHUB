

heroes = list()

while True:
    getInput = input("Enter a Super-Hero: ")
    if getInput == "q":
        break
    heroes.append(getInput)

print(heroes)

#When any output shows this error------------------->
# -----------------------------------------------------
# >>> & C:/Users/HP/python/anaconda/python.exe "d:/python/vscode/python course/3. pandas/dataframes 231021.py"
#   File "<stdin>", line 1
#     & C:/Users/HP/python/anaconda/python.exe "d:/python/vscode/python course/3. pandas/dataframes 231021.py"
#     ^
# SyntaxError: invalid syntax
# -----------------------------------------------------
# Then delete the powershell multiple command windows and fresh run the program,, things will go smooth
