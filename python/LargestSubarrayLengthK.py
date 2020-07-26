class Solution:
    def largestSubarrayLengthKWithoutDup(self, array, k):
        n, idx = len(array), 0
        for i in range(1, n - k + 1):
            if array[i] > array[idx]:
                idx = i
        return array[idx: idx + k]

    def largestSubarrayLengthKWithDup(self, array, k):
        def getVal(ia, ib):
            for i in range(k):
                if array[ia + i] > array[ib + i]:
                    return False
                elif array[ia + i] < array[ib + i]:
                    return True
            return False

        n, idx = len(array), 0
        for i in range(1, n - k + 1):
            if getVal(idx, i):
                idx = i
        return array[idx: idx + k]

if __name__ == '__main__':
    # array has duplicated element?
    # no
    # what's the range of array and k?
    # 1 <= k <= N <= 100
    # 1 <= A[j] <= 1000
    solu = Solution()
    print(solu.largestSubarrayLengthKWithoutDup([1, 4, 3, 2, 5], 4) == [4,3,2,5])
    print(solu.largestSubarrayLengthKWithoutDup([4, 3, 2, 5], 4) == [4, 3, 2, 5])

    # array has duplicated element?
    # no
    # what's the range of array and k?
    # 1 <= k <= N <= 100
    # 1 <= A[j] <= 1000
    solu = Solution()
    print(solu.largestSubarrayLengthKWithDup([4, 4, 3, 2, 5], 4) == [4, 4, 3, 2])
    print(solu.largestSubarrayLengthKWithDup([4, 4, 4, 4, 5], 4) == [4, 4, 4, 5])
    print(solu.largestSubarrayLengthKWithDup([4, 3, 2, 5], 4) == [4, 3, 2, 5])