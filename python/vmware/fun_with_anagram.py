
def fun_with_anagrams(strs):
    res = []
    for st in strs:
        if len(res) == 0 or not anagram(res[-1], st):
            res.append(st)
    return res

def anagram(st1, st2):
    c1, c2 = [0] * 26, [0] * 26
    for ch in st1:
        c1[ord(ch) - ord('a')] += 1
    for ch in st2:
        c2[ord(ch) - ord('a')] += 1

    return c1 == c2

print(fun_with_anagrams(['code', 'doce', 'ecod', 'framer', 'frame']))