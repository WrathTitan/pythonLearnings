num=int(input("Enter a number: "))
print("The divisors of this number are: ")
mydivisors=[]
for n in range(num):
    if((num%(n+1))==0):
        mydivisors.append(n+1)
print(mydivisors)