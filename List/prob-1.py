#Given 2D list calculate the sum of diagonal elements.

#T.C - O(n)
def diagonal_sum(matrix):
    sum=0
    i=0
    for row in matrix:
        sum+=row[i]
        i+=1
    return sum

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print("Diagonal Sum :", diagonal_sum(myList2D))
