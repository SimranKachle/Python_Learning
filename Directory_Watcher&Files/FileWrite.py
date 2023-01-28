import os
def Write_File(FileName):
    if(os.path.exists(FileName)):
        print("Emter data that you want in the file")
        data=input()
        fd=open(FileName,"a")
        fd.write(data)
    else:
        print("File not existing")
        return
def main():
    print("Enter file name to create")
    Name=input()  
    Write_File(Name)
    
if __name__=="__main__":
    main()