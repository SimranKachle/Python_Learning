
class Numbers:
    # pass --> it means kahi nai pudhe ja
    #
    def __init__(self):
        self.Size = 0#instance variable
        self.Arr = list()
        # self.Arr = []

    def Accept(self):
        print("How many elements you want to store?")
        self.Size = int(input())

        print("Please Enter the Elements")
        value = 0
        for i in range(0, self.Size):
            value = int(input())
            self.Arr.append(value)

    def Display(self):
        print("Elements in list are: ")
        for i in range(0, self.Size):#len(self.Arr)
            print(self.Arr[i])

    def Summation(self):
        Sum = 0#local vaiable it is used by the method
        for i in range(0, self.Size):
            Sum = Sum + self.Arr[i]

        return Sum


def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all elements is: ",Output)

if __name__ == "__main__":
    main()
