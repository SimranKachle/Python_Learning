import os
from sys import *


def Directory_Watcher(Dir_Name):
    flag = os.path.isabs(Dir_Name)
    if flag == False:
        path = os.path.abspath(Dir_Name)
    # print("Inside directory wacther method")
    # print("Name of input directory:", Dir_Name)
    exists = os.path.isdir(Dir_Name)
    if exists:
        for foldername, subfolder, Filenames in os.walk(Dir_Name):
            # print("Folder name is: " + foldername)
            for subf in subfolder:
                # print("Subfolder name of "+foldername+"is"+subf)
                for fnames in Filenames:
                    s=fnames.split('.')
                
                    if s[1]==argv[2][1:]:
                        print("file with extention"+argv[2]+" inside "+ foldername+"is"+fnames)
                print(' ')
    else:
        print("invalid path")

def main():
    print("Directory watcher application")

    if(len(argv) < 3):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    try:
        Directory_Watcher(argv[1])
    except ValueError:
         print("Error: Invalid datatype if inpute")
    except Exception as E:
        print("invalid inpute"+E)
    if len(argv)<1 or len(argv)>3:
        print("invalid no of arguments")

if(__name__ == "__main__"):
    main()
