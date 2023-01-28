# def DisplayFactors(No):
#     i=1
#     print("Factors are: ")
  
#     while (i<=int(No/2)):#range automatically increements
        
#         if int(No % i)== 0:
#             print(i) 
        # i=i+1
        
# import numbers
# from numbers import DisplayFactors
# from numbers import *
import numbers as NUM
def main():
    print("Enter number: ")
    No=int(input())
    NUM.DisplayFactors(No)
               
if __name__=="__main__":
    main()