'''

 Author : Dasu Srinivas
 Description : Rotate the given matrix by 90 degrees in clock-wise direction

'''


def rotateClockwise90(mat):
    n = len(mat[0])
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = mat[i][j]
            mat[i][j], mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i] = mat[n-1-j][i], mat[n-1-i][n-1-j], mat[j][n-1-i],temp
    return mat


def rotateAntiClockwise90(mat):
    n = len(mat[0])
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = mat[i][j]
            mat[i][j], mat[j][n-1-i], mat[n-1-i][n-1-j], mat[n-1-j][i] = mat[j][n-1-i], mat[n-1-i][n-1-j], mat[n-1-j][i],temp
    return mat


print(rotateClockwise90([[1,2,3,4],[5,4,3,2],[6,3,8,1],[2,5,7,9]]))

print(rotateAntiClockwise90([[1,2,3,4],[5,4,3,2],[6,3,8,1],[2,5,7,9]]))