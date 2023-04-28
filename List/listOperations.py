#Cretaing a list
integer = [1,2,3,4]
stringList = ['Spam','game','name']
mixList=[1,2,[3,4],'Spam']
print(integer)
print(stringList)
print(mixList)

#Accessing a list element
print("Third element:",mixList[3])

#Traversing a list
for i in mixList:
    print(i)

for i in range(0,len(mixList)):
    print(mixList[i])

#Update/Insert List
myList = [1,2,3,4,5]

#Add element at particular index
myList.insert(2,100)
print(myList)

#Add element at the end of the list
myList.append(230)
print(myList)

#Add new list at the end of the list
myList.extend([111,222,333])
print(myList)

#Slice/Delete from a list
newList = ['a','b','c','d','e']
print(newList[:])

print(newList[3:5])

#Deleting element based on index
newList.pop(3)
print(newList)

#Deleting element based on value of element
newList.remove('b')
print(newList)

#Deleting anelement using del command
del newList[0]
print(newList)

#Deleting using slicing
del newList[0:]
print(newList)