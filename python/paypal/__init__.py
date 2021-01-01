

# 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5
#       |        |        |        |        |
#       0        1        2        3        4

import bisect

# 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, #, #, #, 5, 5
# |        |        |        |        |        |
# 0        1        2        3        4        5

# 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4

def stockLounge(onHand, supplier, demand):
    onHand.sort()
    supplier.sort()
    n = len(onHand)
    m = len(supplier)
    max = (onHand[-1] + 1) * demand

    counter = 0
    i, j = 0, 0
    while i < n:
        if i // demand > onHand[i]:
            counter -= 1
            i -= 1
        elif i // demand < onHand[i]:
            counter += 1
            while j < m and supplier[j] < i // demand:
                j += 1
            if j == m:
                pass
            i += 1
        else:
            i += 1









if __name__ == '__main__':
    res = stockLounge([0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5],
                      [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4], 3)
    print(res)