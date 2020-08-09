


def longestStrChain(words):
    def dfs(word):
        if word in memo:
            return memo[word]
        if len(word) == 1:
            return 1

        res, n = 1, len(word)
        for i in range(n):
            tmp = word[:i] + word[i +1:]
            if tmp in words:
                res = max(1 + dfs(tmp), res)
        memo[word] = res
        return memo[word]

    words = set(words)
    memo = {}
    mx = 0
    for word in words:
        mx = max(mx, dfs(word))
    return mx