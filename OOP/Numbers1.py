
class Numbers:
    # pass --> it means kahi nai pudhe ja
    #
    def __init__(self):
        self.Size = 0
        self.Arr = list()

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
        for i in range(0, self.Size):
            print(self.Arr[i])


def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()


if __name__ == "__main__":
    main()
