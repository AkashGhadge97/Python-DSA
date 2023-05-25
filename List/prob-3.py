# Write a function to remove the duplicate numbers on given integer array/list.

def remove_duplicates(arr):
    newArr = []
    for i in arr:
        if i not in newArr:
            newArr.append(i)
    return newArr 

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
