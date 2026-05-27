tuple1=()                       #Creation of empty tuple
tuple1=(10,20,30,40,20)

# tuple1.add(30) 
# tuple1.remove(10) 
# tuples are immutable we cannot modify them                    

print(tuple1.count(20))             #counts particular element 

print(tuple1[0])                    #tuples support indexing

print(10 in tuple1)                 #membership operators
print(10 not in tuple1)