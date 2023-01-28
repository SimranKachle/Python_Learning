# def DisplayFactors(No):
#     i=1
#     print("Factors are: ")
  
#     while (i<=int(No/2)):#range automatically increements
        
#         if int(No % i)== 0:
#             print(i) 
        # i=i+1

from numbers import *
# import sys
from sys import *
# import numbers as NUM
def main():
    # print("Filename/Application name is : ",argv[0])
    DisplayFactors(int(argv[1]))
               
if __name__=="__main__":
    main()