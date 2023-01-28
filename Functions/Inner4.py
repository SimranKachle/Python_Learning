
def Outer():#100
    print("Inside Outer")
    def Inner():#200
        print("Inside Inner")
        
    print(id(Inner))
    return Inner

ret = Outer()
#return name of inner function. #100()
print(type(ret))
print(id(ret))
ret() #200()#returning func from another func it callls inner call
