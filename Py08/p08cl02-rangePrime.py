# Prime numbers in the range

    
upper_limit = 400
lower_limit = 600


for number in range(lower_limit, upper_limit + 1):
    if number > 1:
        for i in range(2, number):
            if(number % i == 0):
                break
        else:
            print(number)


