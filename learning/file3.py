mylist=[0,1,2,3,4,5]
mydoublelist=map(lambda n: n*2,mylist)
print(mydoublelist)
print(list(mydoublelist))


mynumlist=[90,100,-2,0.75,-55,2]
greater_than_10=list(filter(lambda n:n>10,mynumlist))
print(greater_than_10)