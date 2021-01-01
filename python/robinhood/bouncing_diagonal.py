
def get_weight(matrix, r):
    i, j = r, 0
    n = len(matrix)
    weight = 0
    while i > 0 and j < n:
        weight += matrix[i][j]
        i, j = i - 1, j + 1

    while j < n:
        weight += matrix[i][j]
        i, j = i + 1, j + 1
    return weight

def bouncing_diagonal(matrix):
    n = len(matrix)
    weights = [0] * n
    for i in range(n):
        weights[i] = get_weight(matrix, i)
    values = [row[0] for row in matrix]
    mp = list(zip(weights, values))
    mp.sort()
    print(mp)

bouncing_diagonal([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
