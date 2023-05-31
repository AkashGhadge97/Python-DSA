
#Creating a tuple
newTuple = ('a','b','c','d','e')
print(newTuple)

newTuple1 = tuple('abcde')
print(newTuple1)
print(type(newTuple1))

#Accessing tuple elements
print(newTuple[0])

#Accessing using negative index
print(newTuple[-1])

#Accessing using slice operator
print(newTuple[0:2]) 

#Traversing a tuple
for i in range(len(newTuple)):
    print(newTuple[i])

#Searchan element in a tuple

print('a' in newTuple)

print(newTuple.index('a'))

def searchElement(tup,element):
    for i in range(0,len(newTuple)):
        if tup[i] == element:
            return f"Element present at index {i}"
    return "Element not found!!"

print(searchElement(newTuple, 'a'))    
print(searchElement(newTuple, 'c'))    
    
