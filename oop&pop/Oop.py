#Class =Characteristics+behaviours
#Class = Data+Functions
#Accept 2 numbers and perform addition and subtraction of it



class Arithmetic:
    def __init__(self,A,B):#it is constuctor __ __means special variable
        #self acts as this pointer
        self.No1=A
        self.No2=B
    #A&B are parameters 
    def Add(self):
        return self.No1+self.No2
    
    def Sub(self):
        return self.No1-self.No2

def main():
    print("Enter first number")
    Value1=int(input())
    
    print("Enter Second number")
    Value2=int(input())
    
    obj=Arithmetic(Value1,Value2)
    
    Ans=obj.Add()
    print("Addition is: ",Ans)
    
    Ans=obj.Sub()
    print("Addition is: ",Ans)
    
if __name__=="__main__":
    main()
















