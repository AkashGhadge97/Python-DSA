#Given a n x n matrix print the transpose of the matrix without using any another matrix (i.e in-image)


#Method-1 : Swapping using temp variable
def matrix_transpose(mat):
   for i in range(0,len(mat)):
    for j in range(i,len(mat)):
        temp = mat[i][j]
        mat[i][j] = mat[j][i]
        mat[j][i] = temp 
   return mat

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_transpose(matrix))


#Method-2 : Direct swapping in python
def matrix_transpose(mat):
   for i in range(0,len(mat)):
    for j in range(i,len(mat)):
       mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
   return mat

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_transpose(matrix))
