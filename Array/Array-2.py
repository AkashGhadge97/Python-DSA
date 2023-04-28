from array import *
from cgi import print_arguments
from xml.etree.ElementTree import tostring

# Create an array and traverse it - TC -> O(n)
my_array = array('i', [1, 2, 3, 4, 5, 6])
for i in my_array:
    print(i)

# Accessing individual elements through indexes
print(my_array[0])

# Append any value to the array using append() method
my_array.append(65)
print(my_array)

# Insert value in an array using insert() method
my_array.insert(3, 78)
print(my_array)

# Extend python array using extend() method
my_array.extend([11, 23, 34])
print(my_array)

# Add items to array from list using fromlist() method
tempList = [22, 33, 44, 55]
my_array.fromlist(tempList)
print(my_array)

# Remove an element from array using remove() method
my_array.remove(33)
print(my_array)

# Remove last element from an array using pop() method
my_array.pop()
print(my_array)

# Fetch any element through its index using index() method
print(my_array.index(65))

# Reverese an array
my_array.reverse()
print(my_array)

# Get array buffer information using buffer_info() method
print(my_array.buffer_info())

# Check number of occuramces of an element using count() methdo
print(my_array.count(34))

# Convert python arrayto apython list using tolist() method
lst = my_array.tolist()
print(lst)

# slice elements from an array
print(my_array[1:4])
