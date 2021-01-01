import math

def solution(one, two):
    def solve(a, b, c):
        sol1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        sol2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return sol1, sol2

    def getSum(a, n, d):
        return (n / 2) * (2 * a + (n - 1) * d)

    first = max(one, two)
    second = min(one, two)
    diff = first - second
    v = math.floor(solve(1, 1, -2 * diff)[0])
    first -= getSum(1, v, 1)
    flag = first == second
    v1 = math.floor(solve(1, v, -first)[0])
    v2 = math.floor(solve(1, v + 1, -second)[0])
    first -= getSum(v + 1, v1, 2)
    second -= getSum(v + 2, v2, 2)
    if flag:
        # print(v + v1 + v2 + 1, int(first), int(second))
        return (v + v1 + v2 + 1, int(first), int(second))
    else:
        if one > two:
            # print(v + v1 + v2 + 1, int(first), int(second))
            return (v + v1 + v2 + 1, int(first), int(second))
        else:
            # print(v + v1 + v2 + 1, int(second), int(first))
            return (v + v1 + v2 + 1, int(second), int(first))