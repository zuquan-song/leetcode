
class Solution:

    def shortestSubstring(self, s):
        chs = set()
        for ch in s:
            chs.add(ch)

        counter = {}
        i, j, n = 0, 0, len(s)
        minVal = float('inf')
        while j < n:
            counter[s[j]] = counter.setdefault(s[j], 0) + 1
            while len(counter) == len(chs):
                minVal = min(minVal, j - i + 1)
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    counter.pop(s[i])
                i += 1
            j += 1
        return minVal



if __name__ == '__main__':
    solu = Solution()
    print(solu.shortestSubstring("dabbcabcd"))
