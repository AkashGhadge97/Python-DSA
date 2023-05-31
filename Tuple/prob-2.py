# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

#Solution-1
def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError('Length of the tuples is not same')
    else:
        result = tuple((a+b) for a, b in zip(tuple1, tuple2))
    return result


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

#Solution-2
def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))
