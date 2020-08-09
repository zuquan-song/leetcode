
res = set()
def palindromeSubString(st):
    n = len(st)
    for i in range(n):
        countPalindrome(i, st)
    print(res)
    return len(res)

def countPalindrome(start, st):
    i, j = start, start
    counter = 0
    while i >= 0 and j < len(st):
        if st[i] == st[j] and st[i:j+1] not in res:
            counter += 1
            res.add(st[i:j+1])
        else:
            break
        i, j = i - 1, j + 1

    i, j = start, start + 1
    while i >= 0 and j < len(st):
        if st[i] == st[j] and st[i:j+1] not in res:
            counter += 1
            res.add(st[i:j + 1])
        else:
            break
        i, j = i - 1, j + 1
    return counter

print(palindromeSubString("aabaa"))
