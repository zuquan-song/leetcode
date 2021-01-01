
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = self.parent[rb]

def mini_char_transfer(source, target):
    def unions(ch, d, visited):
        if ch not in d or ch in visited:
            return
        visited.add(ch)
        uf.union(ord(ch), ord(d[ch]))
        unions(d[ch], d, visited)

    def hasLoop(ch, d, visited):
        if ch in visited:
            return True
        if ch not in d:
            return False
        visited.add(ch)
        return hasLoop(d[ch], d, visited)

    d = {}
    res = 0
    for i, ch in enumerate(source):
        if target[i] != ch and ch not in d:
            d[ch] = target[i]
            res += 1
        elif ch in d and d[ch] != target[i]:
            return -1
    uf = UnionFind(128)
    for key in d.keys():
        unions(key, d, set())

    key_set = set(d.keys())
    groups = set()
    for i in range(128):
        if chr(i) in key_set:
            groups.add(uf.find(i))
    loop = 0
    for i in groups:
        if hasLoop(chr(i), d, set()):
            loop += 1

    return res + loop

print(mini_char_transfer("aaa", "bbb"))
print(mini_char_transfer("ababcc", "cccccc"))
print(mini_char_transfer("ab", "ba"))
print(mini_char_transfer("abac", "wxyz"))
# # b->e, a->b, e->a
print(mini_char_transfer("abcd", "badc"))
print(mini_char_transfer("abcdefghijkmabcxyz", "bcdefghijkmabcdbcd"))
print(mini_char_transfer("abcdefgi", "bcdefgha"))