#Problem-2
# Write a program find all pairs of integers whose sum is equal to the given integer
# e.g [2,6,3,9,11]   9 -> [6,3]

#Solution-1 Time Complexity - O(n^2)
def findPairs (arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i]+arr[j] == target :
                print([i,j])

arr = [1,2,3,2,3,4,5,6]
findPairs(arr, 6)
 
print('------------------------------------------------------')
#Solution-2 

def two_sums(arr,target):
    seen = {}
    for i , num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i

arr = [1,2,3,2,3,4,5,6]
findPairs(arr, 5)