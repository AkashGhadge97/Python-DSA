#You are given an n x n 2D matrix  rotate the matrix by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#DO NOT allocate another 2D matrix and do the rotation.


def rotate(matrix):
    for i in range(0,len(matrix)):
        for j in range (i,len(matrix)):
            matrix[i][j] , matrix[j][i] = matrix [j][i] , matrix[i][j]
  
    for row in matrix:
        row.reverse()
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))