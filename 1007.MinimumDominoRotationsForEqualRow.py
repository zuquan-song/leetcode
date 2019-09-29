class Solution:
    def minDominoRotations(self, A, B) -> int:
        n = len(A)
        countA, countB, total = [0] * 7, [0] * 7, [0] * 7

        for i in range(n):
            countA[A[i]] += 1
            countB[B[i]] += 1
            for val in list({A[i], B[i]}):
                total[val] += 1

        if max(total) < n:
            return -1
        maxVal = total.index(max(total))
        return min(n - countA[maxVal], n - countB[maxVal])