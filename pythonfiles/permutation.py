'''def mystring(str):
    return str
print(mystring("Hello"))
Error with this program.
String index out of range
'''
def mypermutation(str,num):
    mylen=len(str)
    maxcases=2**mylen
    if num<=maxcases:
        print(str[num-1]+mypermutation(str[num:],num+1))
    else:
        return str[num-1]
    

mypermutation("abc",1)
