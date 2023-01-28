# class keyword # only functional is not there 
#it is procedural scripting and oop
class Arithmetic:
    # self is a keywork __init__ is special variable
    def __init__(self, A, B):#self keyword is compulsorygeneraly init method if used to crrate instance variables in python
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Substaction(self):
        Ans = self.No1 - self.No2#instance method can access instance variables
        return Ans


def main():#procedural
    print("Inside main method")
    obj = Arithmetic(11, 10)
    # automatically init method in called it is like constuctor after allocating memory for objectobj 
    Output = obj.Addition()
    print("Addition is : ",Output)
    Output = obj.Substaction()
    print("Addition is : ",Output)
    objX = Arithmetic(21,20)

if __name__ == "__main__":#scripting
    print("Inside Starter")
    main()
