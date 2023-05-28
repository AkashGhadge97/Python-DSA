# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# output -> b

def max_value_key(my_dict):
    maxValue = max(my_dict.values())
    for key, value in my_dict.items():
        if value == maxValue:
            return key


my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))


# Solution-2

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)
