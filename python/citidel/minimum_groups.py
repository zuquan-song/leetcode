

# https://www.geeksforgeeks.org/minimum-number-of-groups-of-nodes-such-that-no-ancestor-is-present-in-the-same-group/
def minimumGroups(n, par):
    def findDepth(x, child):
        mx = 0
        for ch in child[x]:
            mx = max(mx, findDepth(ch, child))
        return mx + 1

    child = [[] for _ in range(n + 1)]

    for i in range(n):
        if par[i] != -1:
            child[par[i]].append(i)

    res = 0
    for i in range(n):
        if par[i] == -1:
            res = max(res, findDepth(i, child))
    return res

array = [0, -1, 1, 1, 2, 2, 5, 6]
print(minimumGroups(len(array), array))