'''
	Even or Odd, Divisibility check
'''
num=int(input("Enter number: "))	#int() parse
check=int(input("Enter check: "))
if(num%2==0):				#if condition to check if even
    print("This number is even")	
    if(num%4==0):			#if condition to check if number is divisible by 4
        print("This is divisible by 4")
else:					#else condition
    print("This number is odd")	

if(num%check==0):		#number divisible by check condition
    print("Number is divisible by check")
else:				#else condition
    print("Number not divisible by check")
