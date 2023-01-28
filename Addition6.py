print("Application to demostrate industrial program")
# colon is used for grouping
def main():
    print("Enter First number: ")
    no1=int(input())
    # print(type(no1))
    print("Enter second number: ")
    no2=int(input())
    # print(type(no1))
    Ans=no1+no2#this gives concat as python is considering it as string now we will do typecasting
    
    print("Addition is: ",Ans)
# double underscore or special variable
# == is used for comparison
if __name__ =="__main__" :#: means block has started  
    main()
    # __main__ is inbuilt 