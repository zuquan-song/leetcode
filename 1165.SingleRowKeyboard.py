class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = [0] * 26
        for i, key in enumerate(keyboard):
            index[ord(key) - ord('a')] = i
          
        cur, res = 0, 0
        for ch in word:
            res += abs(index[ord(ch) - ord('a')] - cur)
            cur = index[ord(ch) - ord('a')]
        return res
