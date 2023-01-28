# Function which accept nothing and returns nothing

def Demo1():
    print("Inside Demo1")

# Function accept one parameter and returns nothing


def Demo2(No):
    print("Inside Demo2 with argument: ", No)

# Function accept 1 parameter and return 1 parameter


def Demo3(No):
    print("Inside Demo3 with argument: ", No)
    return No+2

# Function accepts 2 parameters and returns only 1


def Demo4(No1, No2):
    print("Inside Demo4")
    Add = No1+No2  # local variable this will be used only in this block
    return Add


# Function accepts 2 parameters and returns 2 parameters also called as shorthand coding
def Demo5(No1, No2):
    print("Inside Demo5")
    Add = No1+No2
    Sub = No1-No2
    return Add, Sub


def main():
    Demo1()
    Demo2(11)
    Ans = Demo3(10)
    print("Return value of Demo3 is: ", Ans)
    Ans = Demo4(10, 20)
    print("Return value is: ", Ans)

    Ans1, Ans2 = Demo5(11, 10)
    print("First return value: ", Ans1)
    print("First return value: ", Ans2)


if __name__ == "__main__":
    main()
