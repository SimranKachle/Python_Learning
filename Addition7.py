# Now we wiil right reusable code so buisness logic
# is written
# Application must be specific
print("Application to demostrate industrial program")


def Addition(value1, value2):
    Ans = value1 + value2
    
    return Ans


def main():
    print("Enter First number: ")
    no1 = int(input())  # Local variable

    print("Enter second number: ")
    no2 = int(input())

    Sum = Addition(no1, no2)
    print("Addition is: ", Sum)


if __name__ == "__main__":
    main()
