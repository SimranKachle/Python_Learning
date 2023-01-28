
def main():
    print("Enter first number")
    No1 = int(input())

    print("Enter Second number")
    No2 = int(input())

    try:
        Ans = No1/No2
        print("Division is: ", Ans)

    except ZeroDivisionError:
        print("Exception occured")
    
    # except NameError:
    #     print("Exception occured")

    except ValueError:
        print("inside value Error")        

    except Exception:
        print("Inside Last expect Block")
    finally:
        print("Inside finally block")
if __name__ == "__main__":
    main()
