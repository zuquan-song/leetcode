class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j, counters = 0, 0, {}
        mx = 0
        while j < n:
            counters[s[j]] = 1 if s[j] not in counters else counters[s[j]] + 1

            if len(counters) == j - i + 1:
                mx = max(mx, j - i + 1)
            else:
                if counters[s[i]] == 1:
                    counters.pop(s[i])
                else:
                    counters[s[i]] -= 1
                i += 1
            j += 1
        return j - i