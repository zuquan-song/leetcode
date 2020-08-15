
def buildSequence(seq):
    n = len(seq)
    res = []
    for i in range(1, 2 ** n):
        sub, k = "", 0
        while i != 0:
            if i & 1:
                sub = sub + seq[k]
            k, i = k+1, i >> 1
        res.append(sub)
    return sorted(res)

print(buildSequence('xyz'))
print(buildSequence('ba'))
