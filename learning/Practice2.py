num=int(input("Enter number: "))
check=int(input("Enter check: "))
if(num%2==0):
    print("This number is even")
    if(num%4==0):
        print("This is divisible by 4")
else:
    print("This number is odd")

if(num%check==0):
    print("Number is divisible by check")
else:
    print("Number not divisible by check")