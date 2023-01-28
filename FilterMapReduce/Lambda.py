
#Normal Function/Named Function
#def Function_Name(Function_Parameters):
#Function_Body

def Add(No1,No2):
    return No1+No2

#Lambda Functions/Unnamed Functions
#lambda parameters:body

AddFunction=lambda A,B:A+B #It must be in single line

Ans1=Add(10,11)
Ans2=AddFunction(10,11)

print("Addition using normal function: ",Ans1)
print("Addition using normal function: ",Ans2)

print("Type of lambda function is : ",type(AddFunction))