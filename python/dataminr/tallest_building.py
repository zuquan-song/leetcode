import collections

def max_height(N, buildings, heights):
    constraints = dict(zip(buildings, heights))
    constraints[1] = 0

    dp = [float('inf')] * (N+1)
    for i in range(1, N+1):
        dp[i] = min(dp[i-1] + 1, constraints[i] if i in constraints else float('inf'))
    for i in range(N - 1, 0, -1):
        dp[i] = min(dp[i+1] + 1, dp[i])
    return max(dp[1:])

# print(max_height(3, [2, 3], [10000, 10000]))
print(max_height(10, [3, 8], [1, 1]))
# print(max_height(1000, [], []))
# print(max_height(1234, [1, 24, 50, 1000], [10000, 10000, 10000, 10000]))