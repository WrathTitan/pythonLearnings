found=True
i=0
BracketOpen=0
BracketClose=0
stackvalue=0

def checknumber(brackets):
    for i in range(0,len(brackets)-1):
        if(brackets[i]=='['):
            BracketOpen+=1
        if(brackets[i]==']'):
            BracketClose+=1
    
    if(BracketClose==BracketOpen):
        return True
    else:
        return False

def check_balance(brackets):
    if(brackets[0]==']')
        break
    if(checknumber(brackets)):
        for i in range(0,len(brackets)-1):
            if (brackets[i]=='['):
                stackvalue+=1
            if (brackets[i]==']'):
                stackvalue-=1
        if stackvalue==0



            


