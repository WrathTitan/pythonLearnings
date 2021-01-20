def rep_cat(x,y):
    return str(x)*10+str(y)*5
print(rep_cat(3,4))

def factorial(number):
    if (number==1):
        return 1
    return number*factorial(number-1)

print(factorial(5))