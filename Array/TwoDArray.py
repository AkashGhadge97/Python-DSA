from hashlib import new
import numpy as np
twoDArray = np.array([[1, 2, 3, 4], [11, 22, 33, 44], [
                     21, 22, 23, 24], [31, 32, 33, 34]])
print(twoDArray)

# Two add new column hence axis = 1
newTwo2DArray = np.insert(twoDArray, 0, [[34, 23, 45, 66]], axis=1)
print(newTwo2DArray)

# Two add new row hence axis = 0
newTwo2DArray = np.insert(twoDArray, 0, [[34, 23, 45, 66]], axis=0)
print(newTwo2DArray)

# Adding new row at the end of the array
newTwo2DArray = np.append(twoDArray, [[77, 88, 99, 88]], axis=0)
print(newTwo2DArray)

# Traversing two dimensional array


def travesrTwoDArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=" ")
        print()


travesrTwoDArray(twoDArray)

# Searching an element in 2-D array


def searchInTwoDArray(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return 'The value is present at index [' + str(i) + ']['+str(j)+']'


print(searchInTwoDArray(twoDArray, 23))

# Deleting a row from 2-D Array

newArray = np.delete(twoDArray, 0, axis=0)
print(newArray)

# Deleting a column from 2-D Array

newArray = np.delete(twoDArray, 0, axis=1)
print(newArray)
