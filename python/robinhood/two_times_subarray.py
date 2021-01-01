import collections

def subarray(array):
    size = len(set(array))

    counter = collections.defaultdict(int)
    i, j, n = 0, 0, len(array)
    res = 0
    while j < n:
        # print(i, j, counter)
        if len(counter) == size and all(v >= 2 for v in counter.values()):
            res += n - j + 1
            counter[array[i]] -= 1
            # print(counter)
            i += 1
        else:
            counter[array[j]] += 1
            j += 1
    if len(counter) == size and all(v >= 2 for v in counter.values()):
        res += n - j + 1

    return res

if __name__ == '__main__':
    print(subarray([1,1,1,1,1]))
    print(subarray([1,2,2,1,3,3]))