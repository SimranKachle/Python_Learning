from sys import *
from os import *

def Script(No):
    if(No%2==0):
        print("It is even number")
    else:
        print("It is odd")

def main():
    print("-----------------Marvellous Infosystems Automations------------------")
    print("Automation Script started with name: ",argv[0])
    
    if(len(argv)!=2):
        print("Error: Insuffient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()
    
    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help: This Script is used to perform___________")
    
    
    elif((argv[1]=="-u")or(argv[1]=="-U")):
        print("Usage:Provide _________ number of arguments as")
        print("First Argument as:_______ ")
        print("Second Argument as:_______ ")
        exit()
        
    else:
        print("There is no such option in the script as : ",argv[1])
if __name__=="__main__":
    main()