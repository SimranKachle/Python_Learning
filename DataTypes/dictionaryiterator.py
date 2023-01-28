Batches={"PPA":18000,"LB":16700,"Python":16500 ,"Angular":15000}

print("Data of Dictionary: ",Batches)

print("DAta traversal using for loop")

for x in Batches:

  
    print(x)

print("DAta traversal using for loop")    
for x in Batches:
    print(x,Batches[x])
    
print("DAta traversal using for loop")    
for x in Batches:
    print(x,Batches.get(x))
    
keyBatches=Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches=Batches.values()
print(type(valueBatches))
print(valueBatches)

# for i in range(0,len(Batches)):
#     print("BAtch name :",keyBatches[i],end="")
#     print("Fees are: ",valueBatches[i])
for i in range(0,len(Batches)):
    print("Value is :",end="")
   
