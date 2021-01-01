

def divide_array(arr):
    n = len(arr)
    sm = sum(arr) // 2
    dp = [[0] * (sm + 1)] * (n + 1)
    dp[0][0] = True
    mx = -1
    for i in range(1, n + 1):
        for j in range(sm, 0, -1):
            if j - arr[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j - arr[i-1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

            if dp[i][j]:
                mx = max(mx, j)
    return abs(sum(arr) - 2 * mx)

print(divide_array([1,1,2,2,3,3]))
print(divide_array([1,1,2,2,3,3,3]))
# print(divide_array([4,1,-5,1,7,6]))
print(divide_array([1, 4, 7]))
print(divide_array([7, 4, 1]))
print(divide_array([7, 1, 4]))