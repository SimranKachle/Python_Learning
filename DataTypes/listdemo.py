

print("Demonstration of list")
# Data: Heterogeneous
# Indexed:Yes
# Mutable:Yes it can be changed
# Duplicates:Yes
# Ordered:Yes if data is ordered it is indexerd

data = [11,21,51,101]
data1=[11,90.80,True,"Hello"]#Data: Heterogeneous
print("Data is Heterogeneous: ",data1)
print("Data at index 2: ",data[2])
print("Data is Ordered: ",data1)
print("Duplicate elements :",data)

print("List is mutable")
data.append(201)#if data is mutable then only you can append it
print("Data after append: ",data)
data.pop()
print("Data after pop: ",data)
