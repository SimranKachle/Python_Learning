# def Add(No):
#     Ans=0
#     while(No>=0):
#         Ans=Ans + No
#         No=No-1
#     return Ans

def Add(No):
    
    if(No<=0):
        return 0
    else:
        return(No+Add(No-1))
        



Ret = Add(3)

print("Result is: ",Ret)