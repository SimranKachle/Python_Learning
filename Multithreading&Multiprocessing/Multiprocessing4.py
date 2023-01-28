import time
import multiprocessing

def DisplayEven(No):
    for i in range(1, No, 1):
        if (i % 2 == 0):
            print("Even Number: ", i)


def DisplayOdd(No):
    for i in range(1, No, 1):
        if (i % 2 != 0):
            print("Odd Number: ", i)


def main():
    print("Demonstration of Parallel Programming using multiple processes")
    #Target is keyword argument comma is compulsory at the end
    
    Number = 200
    
    p1 = multiprocessing.Process(target = DisplayEven,args=(Number,))
    p2 = multiprocessing.Process(target = DisplayOdd,args=(Number,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    # if no join then control directly goes to next line
    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()#More accurate
    main()#Execution time of process
    end_time = time.process_time()
    print("Executiom time is: ", end_time-start_time)
