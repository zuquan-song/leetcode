

if __name__ == '__main__':
    strs = ["aaa", "bcd", "zzzz", "bcdefg"]
    counter = [[0] * 26 for _ in range(26)]
    dp = [0] * 26

    for str in strs:
        i = ord(str[0]) - ord('a')
        j = ord(str[-1]) - ord('a')
        if i != j:
            counter[i][j] = max(counter[i][j], len(str))
        else:
            counter[i][j] += len(str)
    print(dp)
    print(counter)
    for i in range(26):
        dp[i], tmp = counter[i][i], 0
        for j in range(i):
            tmp = max(dp[j] + counter[l][k] for l in range(j, i + 1) for k in range(l, i + 1))
        dp[i] = tmp
    print(dp[-1])