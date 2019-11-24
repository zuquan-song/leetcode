import collections

class Solution:
    def mostCommonWord(self, paragraph, banned) -> str:
        paragraph = paragraph.lower()
        ban_set = set(banned)

        res_word = ""
        res_freq = 0
        idx = 0
        cur = ""
        freqs = collections.defaultdict(int)
        while idx < len(paragraph):
            if paragraph[idx].isalpha():
                cur += paragraph[idx]
            else:
                if "" != cur and cur not in ban_set:
                    freqs[cur] += 1
                    if freqs[cur] > res_freq:
                        res_freq = freqs[cur]
                        res_word = cur
                cur = ""
            idx += 1
        if "" != cur and cur not in ban_set:
            freqs[cur] += 1
            if freqs[cur] > res_freq:
                res_freq = freqs[cur]
                res_word = cur
        return res_word