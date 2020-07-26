import collections

def kdistinceChars(s, k):
    i, j = 0, k
    dis_chars = collections.Counter(s[:k])
    res = []
    while j <= len(s):
        if len(dis_chars) == k and s[i:j] not in res:
            res.append(s[i:j])
        print(dis_chars)
        dis_chars[s[i]] -= 1
        if dis_chars[s[i]] == 0:
            dis_chars.pop(s[i])
        if j == len(s):
            break
        dis_chars[s[j]] += 1
        i, j = i + 1, j + 1
    return res

if __name__ == '__main__':
    print(kdistinceChars("abcabc", 3))
    print(kdistinceChars("abacab", 3))
    print(kdistinceChars("awaglknagawunagwkwagl", 4))