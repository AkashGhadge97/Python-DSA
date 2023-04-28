import numpy as np
import array

# Creating an array using array module
my_array = array.array('i', [1, 2, 3, 4])
print(my_array)
print(type(my_array))

# Creating an array using  numpy module
np_array = np.array([], dtype=int)
print(np_array)

np_array1 = np.array([1, 2, 3, 4, 5])
print(np_array1)

# insertring an element in an array
my_array.insert(0, 11)
print(my_array)
