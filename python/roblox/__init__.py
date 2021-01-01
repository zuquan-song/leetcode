
def largestSubMat(matrix, maxSum):
    def square(x1, y1, x2, y2):
        return sumGrid[x2][y2] - sumGrid[x1][y2] - sumGrid[x2][y1] + sumGrid[x1][y1]

    n = len(matrix)
    sumGrid = [[0] * (n+1) for _ in range(n+1)]
    res = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            sumGrid[i][j] = sumGrid[i-1][j] + sumGrid[i][j-1] - sumGrid[i-1][j-1] + matrix[i-1][j-1]
            while res < min(i, j) and square(i-res-1, j-res-1, i, j) <= maxSum:
                res += 1
    return res

print(largestSubMat([[2,2,2], [3,3,3],[4,4,4]], 14))