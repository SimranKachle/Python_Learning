# Now we wiil right reusable code so buisness logic is written
# Application must be specific

import marvellousModule
print("Application to demostrate industrial program")




def main():
    print("Value of __name__ from main is : ",__name__)
    print("Enter First number: ")
    no1 = int(input())  # Local variable

    print("Enter second number: ")
    no2 = int(input())

    Sum = marvellousModule.Addition(no1, no2)
    print("Addition is: ", Sum)


if __name__ == "__main__":
    main()
