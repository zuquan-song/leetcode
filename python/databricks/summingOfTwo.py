import collections

def summingOfTwo(input):
    res = 0
    counter = collections.Counter(input)
    iwf = list(zip(counter.keys(), counter.values()))
    n = len(iwf)
    offset = 0
    while offset <= 32:
        val = 2 ** offset
        memo = {}
        for i in range(n):
            v, f = iwf[i]
            if val - v in memo:
                res += memo[val - v] * f
            elif val == v * 2:
                res += f
            memo[v] = f

        offset += 1

    return res

print(summingOfTwo([1, -1, 2, 3])),