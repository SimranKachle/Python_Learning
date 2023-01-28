

print("Demonstration of list")
# Data: Heterogeneous
# Indexed:No
# Mutable:Yes it can be changed
# Duplicates:No
# Ordered:No

data = {11,21,51,101,21,11}
data1={11,90.80,True,"Hello"}
#Data: Heterogeneous
print("First set data with unique elements: ",data)
print("length of data",len(data))
print("Data is Heterogeneous: ",data1)
# print("Data at index 2: ",data1[2])#no square bracket
print("Data is unOrdered: ",data1)
print("Duplicate elements :",data)

print("Set is mutable")
#Insert element in set
data.add(211)
print("Data after insertion: ",data)

data.remove(211)
print("Data after removal: ",data)
data.discard(201)
print("Data after discard: ",data)