import collections

class Trie:
    def __init__(self, ch, isWord):
        self.ch = ch
        self.isWord = isWord
        self.children = {}
        self.word = ""

class Solution:
    def __init__(self):
        self.trie = Trie('#', False)

    def createTrie(self, products):
        for product in products:
            cur = self.trie
            for ch in product:
                if ch not in cur.children:
                    cur.children[ch] = Trie(ch, False)
                cur = cur.children[ch]
            cur.isWord = True
            cur.word = product


    def query(self, word):
        def helper(node, res):
            if node.isWord == True:
                res.append(node.word)
            for ch, child in node.children.items():
                helper(child, res)
        cur = self.trie
        outputs = []
        for ch in word:
            res = []
            if ch not in cur.children:
                return res
            cur = cur.children[ch]
            helper(cur, res)
            res.sort()
            outputs.append(res[:min(len(res), 3)])

        return outputs

if __name__ == '__main__':
    solu = Solution()
    solu.createTrie( ["mobile", "mouse", "moneypot", "monitor", "mousepad"])
    print(solu.query("mouse"))