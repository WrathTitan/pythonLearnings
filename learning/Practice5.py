a=[1,2,3,4,5,6,7,8,9,0,10,292,545,666,-34534]
b=[44,55,22,3,1,4,66,7,8,-666,-34534]
mynewlist=[]
for i in a:
    if(i in b):
        mynewlist.append(i)
print(mynewlist)