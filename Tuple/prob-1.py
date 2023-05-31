# Write a function that calculates the sum and product of all elements in a tuple of numbers.

def sum_product(input_tuple):
    finalProduct = 1
    finalSum = sum(input_tuple)
    for i in input_tuple:
        finalProduct *= i
    return finalSum, finalProduct


input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)
