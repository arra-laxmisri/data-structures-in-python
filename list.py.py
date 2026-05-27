list1=[]                    #empty list creation

list1=[10, 20, 30, 40, 50]
list1.append(60)            #inserting element at end of list
print(list1)

list1.insert(3,35)          #insert(index,value) insert at particular position
print(list1)

list1.pop()                 #removes last element of the list
print(list1)

list1.remove(30)            #remove particular element
print(list1)

list1.extend([40,50,60])    #Used to add multiple elements
print(list1)

print(list1.count(40))      #counts a particular element in list

list1.sort()                #sorts the given list
print(list1)

print(20 in list1)          #membership operators
print(20 not in list1)