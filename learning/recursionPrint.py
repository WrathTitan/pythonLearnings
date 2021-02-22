#Defining a function that prints all the numbers recursively 
def rec_count(number):
    print(number)
    if(number==0):
        return 0
    rec_count(number-1)
    print(number)

mynum=int(input("Enter a number:"))
rec_count(mynum)
