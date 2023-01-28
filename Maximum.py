# Application to findout maximum number

def Maximum(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2


def main():
    print("Enter first number")
    Value1=input()
    
    print("Enter second number")
    Value2=input()
    
    Ans=Maximum(int(Value1),int(Value2))
    print("The Largest Number is : ",Ans)

if __name__=="__main__": #control will directly go to main
    main()