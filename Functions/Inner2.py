
def Demo():
    print("Inside Demo")


def Fun():
    print("Inside Fun")


def Hello(FPTR):#FPTR is place holder
    print("Inside Hello")
    FPTR()


Hello(Demo)
Hello(Fun)
# Hello(11)