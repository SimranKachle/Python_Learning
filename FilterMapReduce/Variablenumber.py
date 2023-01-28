def Add(*Values):
    sum=0
    
    for no in Values:
        sum=sum+no
    return sum

def AddX(*Values):
    sum=0
    
    for i in range(0,len(Values),1):
        sum=sum+Values[i]
    return sum



def main():
    Ans=AddX(10,11,1,9)
    print("Addition is: ",Ans)

if __name__=="__main__":
    main()