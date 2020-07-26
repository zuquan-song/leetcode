class Solution():
    def compareString(self, A, B):
        def countFreq(s):
            counter = [0] * 26
            for ch in s:
                counter[ord(ch) - ord('a')] += 1
            for c in counter:
                if c != 0:
                    return c
            return 0
        strsA = A.split(" ")
        strsB = B.split(" ")
        # since the length of every element <= 10
        # buckets is the counter of C[j] of bucket
        # if "AA AAAABB AAC" then buckets [0, 0, 3, 0, 1, ...]
        buckets = [0] * 11
        for s in strsA:
            buckets[countFreq(s)] += 1

        for i in range(1, len(buckets)):
            buckets[i] = buckets[i - 1] + buckets[i]

        res = []
        for s in strsB:
            res.append(buckets[countFreq(s) - 1])
        print(res)
        return res


if __name__ == '__main__':
    # what's the range of A, B
    # N length of A and M is the length of B
    # 1 <= N, M <= 10000
    # For every string in every string in A, B, the range k is 1<= k <= 10
    # return: number of counters which a strictly smaller than B
    solu = Solution()
    solu.compareString("abcdd abc", "hhhhjk yyghhhh aaaaaa")
    solu.compareString("abcd aabc bd", "aaa aa")