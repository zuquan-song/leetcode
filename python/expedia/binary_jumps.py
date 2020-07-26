import collections

class Solution:
    def binaryJumps(self, n, str):
        last0 = -1
        last1 = -1
        result = float('-inf')
        for i, ch in enumerate(str):
            if ch == '0':
                result = max(result, i - last0)
                last0 = i
            elif ch == '1':
                result = max(result, i - last1)
                last1 = i
        return result

if __name__ == '__main__':
    edges = [[1, 2], [2, 1], [2, 4], [2, 5], [3,2], [3, 5], [4, 2], [4, 5], [5, 2], [5, 3], [5, 4], [5, 6], [6,4], [6,5]]

    solu = Solution()
    print(solu.binaryJumps(5, "10101"))