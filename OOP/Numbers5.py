class Numbers:
      
    def __init__(self):
        self.Size = 0  # instance variable
        self.Arr = list()
        # self.Arr = []
        self.Accept()

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
        for i in range(0, self.Size):  # len(self.Arr)
            print(self.Arr[i])

    def Summation(self):
        Sum = 0  # local vaiable it is used by the method
        for i in range(0, self.Size):
            Sum = Sum + self.Arr[i]

        return Sum

    def Average(self):
        Sum = 0  # local vaiable it is used by the method
        for i in range(0, self.Size):
            Sum = Sum + self.Arr[i]

        return (Sum/self.Size)

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0, self.Size):
            if (self.Arr[i] > Max):
                Max = self.Arr[i]

        return Max

    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0, self.Size):
            if (self.Arr[i] < Min):
                Min = self.Arr[i]

        return Min
    
    
def main():
    obj = Numbers()
    # obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all elements is: ", Output)

    Output = obj.Average()
    print("Average of all elements is: ", Output)

    Output = obj.Maximum()
    print("Maximum element is: ", Output)

    Output = obj.Minimum()
    print("Minimum element is: ", Output)

if __name__ == "__main__":
    main()
