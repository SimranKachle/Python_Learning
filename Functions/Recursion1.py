
# def Display(No):
#     Cnt=0
#     if(Cnt<No):
#         print("Hello")
#         Cnt=Cnt+1
#         Display(No)
        
# Display(4)


def Display(No):
    
    if(No>0):
        print("Hello")
        No=No-1
        Display(No)#Recursive function call
        
Display(4)