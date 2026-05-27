dict1=dict()
dict1={}                #Creation of Empty dictionary

dict1={"name": "Latha" , "age": 15}

print(dict1)            #Prints the dictionary

print(dict1.keys())     #print keys only

print(dict1.values())   #print values only

print(dict1.items())    #print keys and values

print(dict1['name'])     #print the value of the key

dict1['city']='hyderabad' #adding a key-value pair
print(dict1)

dict1['age']=18           #modifying existing key-value pair
print(dict1)

del dict1['age']          #delete a particular key-value pair
print(dict1)

print("name" in dict1)    #membership operators

for key in dict1.keys():
    print(key)
