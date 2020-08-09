
# https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/
def palindromeSubString(st):
    res = 0
    n = len(st)
    for i in range(n):
        res += countPalindrome(i, st)
    return res

def countPalindrome(start, st):
    i, j = start, start
    counter = 0
    while i >= 0 and j < len(st):
        if st[i] == st[j]:
            if j - i >= 1:
                counter += 1
        else:
            break
        i, j = i - 1, j + 1

    i, j = start, start + 1
    while i >= 0 and j < len(st):
        if st[i] == st[j]:
            if j - i >= 1:
                counter += 1
        else:
            break
        i, j = i - 1, j + 1
    return counter

print(palindromeSubString("abaab"))
print(palindromeSubString("abbaeae"))