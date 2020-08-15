
def budgetshopping(n, quantities, costs):
    dp = [-1] * (n+1)
    dp[0] = 0

    for i in range(1, n):
        for j, cost in enumerate(costs):
            if cost <= i:
                dp[i] = max(dp[i], dp[i-cost] + quantities[j])
    return dp[-1]