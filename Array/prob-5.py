#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

#Solution-1
def middle(lst):
    lst.pop()
    lst.pop(0)
    return lst

lst = [6,1,22,3,4]

print(middle(lst))

#Solution-2

def middle_new(lst):
    return lst[1:-1]

lst_new = [5,3,6,7,2,3,4]
print(middle_new(lst_new))
