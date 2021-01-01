import collections

def anagram(arr):
    counter = collections.Counter()
    for val in arr:
        counter["".join(sorted(str(val)))] += 1

    print(counter)
    res = 0
    for k, v in counter.items():
        res += v * (v-1) // 2

    return res


if __name__ == '__main__':
    print(anagram([25, 35, 872, 228, 53, 278, 872]))