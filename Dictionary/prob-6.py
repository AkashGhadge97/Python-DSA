# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

def check_same_frequency(list1, list2):
    return sorted(list1) == sorted(list2)


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))


# Solution-2 Using dictionary

def check_same_frequency(list1, list2):
    def count_elements(list):
        counter = {}
        for element in list:
            counter[element] = counter.get(element, 0)+1
        return counter
    return count_elements(list1) == count_elements(list2)


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))
