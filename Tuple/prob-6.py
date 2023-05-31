# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

# Solution-1
def common_elements(tuple1, tuple2):
    lst = []
    for i in tuple1:
        if i in tuple2:
            lst.append(i)
    return tuple(lst)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)

# Solution-2


def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))
