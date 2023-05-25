#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Input: nums = [1,2,3,1]
#Output: true

def contains_duplicate(nums):
    toSet = set(nums)
    if len(toSet) == len(nums):
        return False
    else:
        return True
        
print(contains_duplicate([1,2,3,1]))