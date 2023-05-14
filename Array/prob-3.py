import numpy as np

#How to check if an array contains a number in python
arr = np.array([1,2,3,4,5,6,7,8,9,10])

def findNumber(arr,num):
    for i in range(0,len(arr)):
        if arr[i] == num:
            return f"Element present at index {i}"
        
    return "Element doesn't exist"        

print(findNumber(arr, 11))