
def maxOfMinAltitudes(grid):
    m, n = len(grid), len(grid[0])
    def dfs(i, j, minVal, grid):
        if i == m - 1 and j == n - 1:
            return min(grid[i][j], minVal)

        minVal = min(grid[i][j], minVal)
        if i == m - 1:
            return dfs(i, j + 1, minVal, grid)
        elif j == n - 1:
            return dfs(i + 1, j, minVal, grid)
        else:
            return max(dfs(i + 1, j, minVal, grid), dfs(i, j + 1, minVal, grid))
    return dfs(0, 0, float('inf'), grid)

def maxOfMinAltitudes2(matrix):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = min(matrix[i][j], matrix[i][j - 1])
            elif j == 0:
                dp[i][j] = min(matrix[i][j], matrix[i - 1][j])
            else:
                dp[i][j] = min(matrix[i][j], max(dp[i - 1][j], dp[i][j - 1]))

    return dp[-1][-1]

if __name__ == '__main__':
    print(maxOfMinAltitudes2([[5, 1], [4, 5]]))
    print(maxOfMinAltitudes2([[1, 2, 3], [4, 5, 1]]))