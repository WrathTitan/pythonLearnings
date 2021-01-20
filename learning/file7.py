n=50
num_list=[10,4,23,6,18,27,47]
result=()
found=False
for n1 in num_list:
    for n2 in num_list:
        if(n1+n2==n):
            result=(n1,n2)
            found=True
            break
if found==True:
    print(result)


num_list1=range(0,10)
for n in num_list1:
    if (n==3 or n==6 or n==9):
        continue
    print(n)
