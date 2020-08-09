import math

# https://leetcode.com/problems/consecutive-numbers-sum/

def consecutiveNumbersSum(N: int) -> int:
    count = 0
    for i in range(1, int(math.sqrt(2 * N)) + 1):
        if (2 * N - i * (i - 1)) % (2 * i) == 0:
            count += 1
    return count