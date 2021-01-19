a=[1,1,2,3,5,8,13,21,34,55,89,1,-5,-10,-100,5,4,3,3,1,2]
mynewlist=[]
mynum=int(input("Enter a number: "))
print("The numbers that are less than 5: ")
for n in a:
    if(n<5):
        print(n,end="")
        mynewlist.append(n)
print("\nList of numbers less than 5: ")
print(mynewlist)
mynewlist2=[]
for m in a:
    if(m<5):
        mynewlist2.append(m)

print("The list of numbers that are less than",mynum)
