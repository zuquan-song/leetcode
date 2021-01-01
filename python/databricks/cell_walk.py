

def cell_walk(matrix):
    n = len(matrix)
    res = []
    for start in range(n):
        i, j, value = start, 0, 0
        while i > 0:
            value += matrix[i][j]
            i, j = i - 1, j + 1

        while j < n:
            value += matrix[i][j]
            i, j = i + 1, j + 1
        res.append((value, start))
    res.sort(key=lambda x: (-x[0], -x[1]))
    return [r[1] for r in res]

print(cell_walk([[2, 3, 2], [0, 2, 5], [1, 0, 1]]))