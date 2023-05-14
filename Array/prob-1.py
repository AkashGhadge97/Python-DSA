#Problem-1
# Write a function to find the missing number in a given integer array of 1 to 100.

#Solution-1 - Time Complexity : O(n)
def missing_number(arr, n):
    # TODO
    for i in range(1,n):
        if i in arr:
            continue
        else:
            break
    return i

print(missing_number([1,2,3,5,6,7,8,9],10))


#Solution-2  - Time Complexity  - O(1)  -> Optimla Solution
def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing
 
# Example
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5