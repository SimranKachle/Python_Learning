from operator import truediv


def CheckEven(No):
    if(No%2==0):
        return True
    else:
        return False
    
def CheckEvenX(No):
    return(No%2==0)
    
Ret=CheckEvenX(12)

if(Ret==True):
    print("It's Even")
else:
    print("It's Odd")