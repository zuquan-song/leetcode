class Solution:
    def minDominoRotations(self, A, B) -> int:
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] != x:
                    rotations_a += 1
                if B[i] != x:
                    rotations_b += 1
            return min(rotations_a, rotations_b)

        n = len(A)
        rotations = check(A[0])
        # if we cannot find a rotation or A[0] == B[0], the result is rotation
        if rotations != -1 or A[0] == B[0]:
            return rotations
        # else tells us the rotation is -1 and A[0] != B[0]
        else:
            return check(B[0])