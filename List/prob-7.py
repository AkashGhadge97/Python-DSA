#String permutations
#Given two string check if those are permutations of each other\

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
str1 = 'akash'
str2= 'shaak'
list1 = list(str1)
list2 = list(str2)
print(check_permutation(list1, list2))