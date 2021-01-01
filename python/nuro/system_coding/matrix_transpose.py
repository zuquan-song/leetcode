import math

# len = ceil(m / k)
def split(start, l, old, new):
    m, n = len(old), len(old[0])
    for i in range(start, min(start + l, m)):
        for j in range(n):
            new[j][i] = old[i][j]
    return new


def transpose(matrix, k):
    m, n = len(matrix), len(matrix[0])
    nmat = [[0] * m for _ in range(n)]
    l = math.ceil(m / k)
    for i in range(k):
        split(i * l, l, matrix, nmat)
    return nmat

print(transpose([[1,2,3,7],[4,5,6,8]], 2))