'''
	Palindrome check using for loops
'''
mystr=input("Enter a string: ")
count=0
for i in range(len(mystr)):
    if(mystr[i]==mystr[len(mystr)-i-1]):	#checking if the first and the last elements of the string are same or not
        count+=1	#count is incremented if the characters are equal
if(count==len(mystr)):		#if count is the same as the length then it is a palindrome
    print("Palindrome")
else:
    print("Not a palindrome")
