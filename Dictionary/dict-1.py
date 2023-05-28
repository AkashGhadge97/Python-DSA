

myDict = {'name': 'Akash', 'Age': 20, 'Address':  'India'}
print(myDict)

# Inserting analemenet in a dictionary
myDict['City'] = 'Satara'
print(myDict)

# Updating an element in a dictionary
myDict['Age'] = 30
print(myDict)

# Deleting an element in a dictionary by specifying key to del keyword
del myDict['Age']
print(myDict)

# Deleting an element in a dictionary usin pop method
removed_element = myDict.pop('Address')
print(myDict)
print(removed_element)

# Delete all the elements from a dictionary
myDict.clear()
print(myDict)


# Traversing a dictionary
myDict = {'name': 'Akash', 'Age': 20, 'Address':  'India'}


def traversDict(dict):
    for key, value in dict.items():
        print(key, value)
    print(dict.keys())
    print(dict.values())


traversDict(myDict)
