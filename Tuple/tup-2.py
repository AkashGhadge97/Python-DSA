#Concatenate  two tuple

tup1 = (1,2,3,1,4,5)
tup2 = (1,2,5,2,3,5)
print(tup1 + tup2)

#Repetation of tuple using *

print(tup1 * 4)

# In Operator
print(4 in tup1)

# count() - counts the number of occurances of specified element
print(tup1.count(1))

#index() - return the index of specified element
print(tup1.index(4))

#len() - returns the length of tuple
print(len(tup1))

#max() - Rteuns the max element
print(max(tup1))

#min() - Rteuns the min element
print(min(tup1))

#tuple() method

lst= [3,2,4,5]
print(tuple(lst))
