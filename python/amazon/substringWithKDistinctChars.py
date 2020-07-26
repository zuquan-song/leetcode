import collections


class Solution:
    def subarraysWithKDistinct(self, A, K) -> int:
        def atMost(array, k):
            i, res, dis = 0, 0, 0
            counter = collections.Counter()
            for j in range(len(array)):
                counter[array[j]] += 1
                if counter[array[j]] == 1:
                    dis += 1

                while dis > k:
                    counter[array[i]] -= 1
                    if counter[array[i]] == 0:
                        dis -= 1
                    i += 1
                res += j - i + 1
            return res

        return atMost(A, K) - atMost(A, K - 1)