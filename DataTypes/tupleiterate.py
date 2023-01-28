# Data: Heterogeneous
# Indexed:Yes
# Mutable:No
# Duplicates:Yes
# Ordered:Yes if data is ordered it is indexerd

Data = (11,21,51,101)

print("Output using for")
for no in Data:
    print(no,end=" ")#Print in one line not on next line
print("\n----------------------------------")

print("Output using for with index")
for i in range(0,len(Data)):
    print(Data[i],end=" ")#Print in one line not on next line
print("\n----------------------------------")

print("Output using while with index")
i=0
while(i<len(Data)):
    print(Data[i],end=" ")
    i+=1
print("\n-------------------------------------")