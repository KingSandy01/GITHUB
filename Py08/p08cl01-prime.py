# find if the number is a prime number

def primeNumber():
    t = n
    if t > 1:
        for i in range(2, t):
            if(t%i==0):
                print(t, ", is not a prime number.")
                print(i, "times", t//i, "is", t)
                break
        else:
            print(t, "is a prime number.")


n = eval(input("Enter the number to check for Prime: "))
primeNumber()