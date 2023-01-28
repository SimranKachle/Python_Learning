def CheckEvenX(No):
    return(No%2==0)

# lamda parameter:body
Even =lambda No : No % 2 == 0    
Ret=Even(12)

if(Ret==True):
    print("It's Even")
else:
    print("It's Odd")