# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# Output - {1: 'a', 2: 'b', 3: 'c'}

def reverse_dict(my_dict):
    newDict = {}
    for k, v in my_dict.items():
        newDict[v] = k
    return newDict


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))


# Solution-2 with more space optimization
def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))
