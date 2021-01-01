import collections

def findIndex(st, queries):
    charIndex = [[] for _ in range(26)]
    charDict = {}

    for i, ch in enumerate(st):
        chars = charIndex[ord(ch) - ord('a')]
        chars.append(i)
        charDict[i] = len(chars) - 1

    res = []
    for idx in queries:
        ch = st[idx]
        chars = charIndex[ord(ch) - ord('a')]
        subIdx = charDict[idx]

        nearest = -1
        if subIdx > 0:
            nearest = chars[subIdx - 1]

        if subIdx < len(chars) - 1 and (nearest == -1
                    or abs(nearest - chars[subIdx]) > abs(nearest - chars[subIdx + 1])):
            nearest = chars[subIdx + 1]

        res.append(nearest)
    return res

print(findIndex("leetcode", [2, 3, 7]))
