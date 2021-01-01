

def contitious_subarray_check(a, b, c):
    c = set(c)
    if any(e not in c for e in b):
        return False

    na, nb = len(a), len(b)
    ruleB = False
    for i in range(na - nb + 1):
        if a[i: i+nb] == b:
            ruleB = True
    if not ruleB:
        return False

    i, j = 0, 0
    while j < na:
        if a[j] in c:
            j += 1
            if j - i > nb:
                return False
        else:
            j += 1
            i = j

    return True


if __name__ == '__main__':
    res = contitious_subarray_check([1,1,5,1,2], [1,2], [2,1])
    print(res)