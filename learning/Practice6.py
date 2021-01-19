mystr=input("Enter a string: ")
count=0
for i in range(len(mystr)):
    if(mystr[i]==mystr[len(mystr)-i-1]):
        count+=1
if(count==len(mystr)):
    print("Palindrome")
else:
    print("Not a palindrome")