def factorial(No):
    
    if(No<=0):
        return 1
    else:
        return(No*factorial(No-1))
        



Ret = factorial(5)

print("Result is: ",Ret)