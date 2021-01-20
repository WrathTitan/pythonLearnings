'''def mystring(str):
    return str
print(mystring("Hello"))'''
def mypermutation(str,num):
    mylen=len(str)
    maxcases=2**mylen
    if num<=maxcases:
        print(str[num-1]+mypermutation(str[num:],num+1))
    else:
        return str[num-1]
    

mypermutation("abc",1)