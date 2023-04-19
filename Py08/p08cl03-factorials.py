# Factorials
# Only available to positive 

# for negative = NO 
# for 0 : 1
# for example: 5
# 1*2*3*4*5

number = 4

f = 1

if number < 0:
    print("Negative numbers have no factorials.")
elif number == 0:
    print("The result is = 1")
else:
    for i in range(1,number + 1):
        f = f*i
    print("The factorial is", f)





