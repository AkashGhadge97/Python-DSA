# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

# Solution-1
def get_diagonal(tup):
    lst = []
    index = 0
    for i in tup:
        lst.append(i[index])
        index += 1
    return tuple(lst)


input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)


# Solution-2
def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))
