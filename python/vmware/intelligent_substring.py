
def intelligent_substring(s, k, charValue):
    l, r = 0, 0
    chars = 'abcdefghijklmnopqrstuvwxyz'
    normals = set()
    for i, v in enumerate(s):
        if s[i] == '0':
            normals.add(chars[i])
    counter = 0
    n = len(charValue)
    while r < n:
        if charValue[r] in normals:
            counter += 1

        r += 1
        if counter > k:
            if charValue[l] in normals:
                counter -= 1
            l += 1
    return r - l


print(intelligent_substring('10101111111111111111111111', 2, 'abcde'))
print(intelligent_substring('10101111111111111111111111', 1, 'abcde'))