

def prison(n, m, h, v):
    hset = set(h)
    vset = set(v)

    l, mxh = 0, 1
    for i in range(1, n+2):
        if i not in hset or i == n:
            mxh = max(mxh, i - l)
            l = i

    u, mxv = 0, 1
    for i in range(1, m+2):
        if i not in vset or i == m:
            mxv = max(mxv, i - u)
            u = i
    return mxh * mxv

if __name__ == '__main__':
    print(prison(3, 2, [1,2,3], [1,2]))