#Problem - Given an array return the maximum product of two integers in an array where all elements are positive.

arr = [3,2,4,5,6,7,8,9]
def maxProduct(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

print("Max Product :",maxProduct(arr))

#Solution without any in-built function - T.C =  O(n)  | S.C -  O(1clear
# )

def max_product(arr):
    max1,max2 = 0, 0

    for num in arr:
        if num > max1:
            max2=max1
            max1=num
        elif num > max2:
            max2=num

    return max1*max2


print("Max Product :",max_product(arr))