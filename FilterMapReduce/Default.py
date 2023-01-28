

def Area(Radius, PI=3.14):  # default must be at the end
    Result = PI*Radius*Radius
    return Result


def main():
    RValue = 10.5
    PIValue = 3.14

    Ans = Area(RValue, PIValue)  # Ans=Area(10.5,3,14)This is positional
    print("Area of circle is: ", Ans)

    Ans = Area(Radius=RValue, PI=PIValue)  # keyword argument
    print("Area of circle is: ", Ans)

    Ans = Area(10.5)  # positional+default
    print("Area of circle is: ", Ans)

    Ans = Area(Radius=10.5)  # keyword+Default
    print("Area of circle is: ", Ans)

    Ans = Area(PI=7.10, Radius=10.5)  # Keyword arguments
    print("Area of circle is: ", Ans)


if __name__ == "__main__":
    main()
