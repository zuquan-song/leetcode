
class TrieNode:
    def __init__(self, ch, leaf=False):
        self.ch = ch
        self.isLeaf = leaf
        self.children = {}

    def contains(self, ch):
        return ch in self.children

    def append(self, ch):
        self.children[ch] = TrieNode(ch)

    @classmethod
    def longestPrefix(cls, root, st):
        res = ""
        cur = root
        for ch in st:
            if ch not in cur.children:
                break
            cur = cur.children[ch]
            res += ch
        return res


def longest_prefix(codes, phones):
    root = TrieNode('', False)
    for code in codes:
        cur, n = root, len(code)
        for i, ch in enumerate(code):
            if not cur.contains(ch):
                cur.append(ch)
            cur = cur.children[ch]
        cur.isLeaf = True

    res = []
    for phone in phones:
        res.append(TrieNode.longestPrefix(root, phone))
    return res

print(longest_prefix(["213", "21358", "1234", "12"], ["21349049", "1204539492", "123490485904"]))