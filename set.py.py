set1=set()                          #Creation of empty set

set1={10,20,30,40}                  #No duplicates are allowed(Unique values only)
print(set1)

set1.add(50)                        #Adding 50 into the set
print(set1)

set1.discard(10)                     #removes particular element
print(set1)

#print(set1.remove(10))             What does it return?

print(70 in set1)
print(70 not in set1)               #membership operators 