import functools

def attack_prob2(N, M, K):
    dp = [[0] * (K+1) for _ in range(N+1)]
    for i in range(K+1):
        dp[0][i] = 1

    colSum = [[0] * (K+1) for _ in range(N+1)]
    for i in range(K+1):
        colSum[0][i] = 1
    for i in range(N+1):
        colSum[i][0] = 1
    for n in range(1, N+1):
        for k in range(1, K+1):
            if n > M:
                dp[n][k] += (colSum[n][k - 1] - colSum[n - M - 1][k - 1]) / (M + 1)
            else:
                dp[n][k] += (colSum[n][k - 1]) / (M + 1)

            if M > n:
                dp[n][k] += (M-n) / (M+1)
            colSum[n][k] = colSum[n-1][k] + dp[n][k]

    return dp[N][K]

def attack_prob(N, M, K):
    @functools.lru_cache(None)
    def dfs(n, k):
        if n == 0:
            return 1
        if k == 0:
            return 0
        res = 0
        for i in range(min(M+1, n+1)):
            res += dfs(n-i, k-1) * 1/(M+1)
        if M > n:
            res += (M-n)/(M+1)
        return res
    return dfs(N, K)



# print(attack_prob2(1000, 1000, 1000))
print(attack_prob2(2, 1, 3))
print(attack_prob2(2, 1, 4))
print(attack_prob2(2, 1, 5))
print(attack_prob2(3, 2, 3))