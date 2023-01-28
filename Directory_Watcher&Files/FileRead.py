import os


def Read_File(FileName):
    if(os.path.exists(FileName)):
        print("Emter data that you want in the file")
        fd = open(FileName, "r")
        Data = fd.read()
        print("Data from file is ")
        print(Data)
        fd.close()
    else:
        print("File is not existing")
        return


def main():
    print("Enter file name to create")
    Name = input()
    Read_File(Name)


if __name__ == "__main__":
    main()
