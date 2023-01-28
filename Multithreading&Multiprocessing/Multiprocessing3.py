import time


def DisplayEven(No):
    for i in range(1, No, 1):
        if (i % 2 == 0):
            print("Even Number: ", i)


def DisplayOdd(No):
    for i in range(1, No, 1):
        if (i % 2 != 0):
            print("Odd Number: ", i)


def main():
    print("Demonstration of Serial Programming")
    DisplayEven(20)
    DisplayOdd(20)
    # DisplayEven(2000)
    # DisplayOdd(2000)


if __name__ == "__main__":
    start_time = time.process_time()#More accurate
    main()#Execution time of process
    end_time = time.process_time()
    print("Executiom time is: ", end_time-start_time)