class Solution:
    def maxProfit(self, trans: int, prices) -> int:
        # DP[i][j] mean maxprofit at i-th transaction, sell at j-th day
        n = len(prices)
        if trans >= n // 2:
            # this is for quick solution because while trans >= n // 2,
            # which means you can buy at day t and sell at day t+1,
            # eg: trans=4, n=4, you can buy day 1 sell day 2, buy day 3 sell day 4
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        dp = [[0] * n for _ in range(min(n, trans) + 1)]
        for i in range(1, trans + 1):
            mx = -prices[0]
            for j in range(1, n):
                # this is the most interesting part, because the original transfer formular is
                # dp[i][j] = max(dp[i][j - 1], dp[i - 1][t - 1] + prices[j] - prices[t]) t from 0 -> j
                # the part could be like: prices[j] + max(dp[i - 1][t - 1] - prices[t]) t from 0 -> j
                # since we have duplicated calculate while j traverse 0->j, because: max(dp[i - 1][t - 2] - prices[t-2])
                # eg: dp[i-1]: 3,6,4,7,2
                #     prices:  4,5,6,7,8,
                # when calculate maxVal, dp[i - 1][t - 1] - prices[t-1] will be calculated at most o(t) times, which is not necessary
                # so using a temp value mx to calculate max dp[i - 1][j - 1] - prices[j] will save the last max value

                dp[i][j] = max(dp[i][j - 1], prices[j] + mx)
                mx = max(mx, dp[i - 1][j - 1] - prices[j])
        return dp[trans][n - 1]
