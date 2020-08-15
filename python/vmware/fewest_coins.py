
def fewest_coins(coins):
    chs = set()
    for ch in coins:
        chs.add(ch)
    n = len(chs)
    counters = {}

    i, j = 0, 0
    res = float('inf')
    while j < len(coins):
        if len(counters) != n:
            counters[coins[j]] = counters.setdefault(coins[j], 0) + 1
            j += 1
        while len(counters) == n:
            counters[coins[i]] = counters[coins[i]] - 1
            if counters[coins[i]] == 0:
                counters.pop(coins[i])
            res = min(res, j - i)
            i += 1
    return res

print(fewest_coins('dabbcabcd'))
