#Permutations
#Given two list check of those are permutation of each other

def check_permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    else:
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False

print(check_permutation([1,2,3],[2,3,1]))      