import os


def DeleteFile(FileName):

    if(os.path.exists(FileName)):
        size=os.path.getsize(FileName)
        if(size==0):
            os.remove(FileName)
        else:
            print("Are you sure to delete the file?Y/n?")
            option=input()
            if(option=="Y"or option=="y"):
                os.remove(FileName)
            else:
                print("File deletion process stoppes.")
    else:
        print("There is no such FIle")
            
def main():
    print("Enter file name to create")
    Name = input()
    DeleteFile(Name)


if __name__ == "__main__":
    main()
