# Dictionary Methods

# fromkeys()
newDict = {}.fromkeys([1, 2, 3], 0)
print(newDict)

# copy()
dict1 = {'name': 'Akash', 'Age': 25, 'address': 'satara'}
dict2 = dict1.copy()
print(dict2)

# get()
print(dict1.get('Age'))
print(dict1.get('city', 'satara'))

# items()
print(dict1.items())

# keys()
print(dict1.keys())

# values()
print(dict1.values())

# popitem()
print(dict1.popitem())
print(dict1)

# setdefault()
print(dict1.setdefault('name', 'John'))
print(dict1.setdefault('city', 'satara'))
print(dict1)

# pop()
dict1.pop('city')
print(dict1)

dict3 = {'1': 1, '2': 2, '3': 3}
dict1.update(dict3)
print(dict1)
