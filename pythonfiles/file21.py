myarr=[2,4,5,6,8,1,2,5,4,3,3,4]
print(myarr)

myarr.sort()
print(myarr)

mylen=len(myarr)

mymap=dict()

for i in range(mylen):
    if myarr[i] in mymap.keys():
        mymap[myarr[i]]+=1
    else:
        mymap[myarr[i]]=1

max_count=0
res=1

for i in mymap:
    if(max_count<mymap[i]):
        res=i
        max_count=mymap[i]
print(res)

print(mymap)