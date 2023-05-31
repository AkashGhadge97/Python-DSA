# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
def insert_value_front(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple


input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)
