
import Substraction

def Decorated_Function(Function_Name):#200
    def Inner(A, B):#300
        if(A < B):
            A, B = B, A  # multiassignment values copy hojaate hai
        Output = Function_Name(A, B)#200(12,8)
        return Output
    return Inner #return 300


def main():#100
    Value1 = int(input("Enter first Number: "))
    Value2 = int(input("Enter Second Number: "))

    New_Function = Decorated_Function(200)#Decorated_Function(Substraction)
    Ret=(New_Function(Value1, Value2))#Ret=300(8,22)
    print(Ret)


if __name__ == "__main__":
    main()#call 100




