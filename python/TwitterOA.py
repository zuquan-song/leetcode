import collections

def solve(k, numbers):
    n = len(numbers)
    if n%k != 0:
        return "No"
    counters = collections.Counter(numbers)
    if max(counters.values()) > n//k:
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    print(solve(2,[1,2,3,4]))
    print(solve(2,[1,2,2,4]))