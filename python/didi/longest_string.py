import collections

def longest_string_array(arr):
    def helper(arr, prefix):
        if len(arr) == 0:
            return len(prefix)

        res = float('-inf')
        for i, st in enumerate(arr):
            counter = collections.Counter(st)
            if len(counter) == len(st) and all(ch not in prefix for ch in st):
                length = helper(arr[i+1:], prefix + st)
                res = max(res, length)
        return res
    return helper(arr, "")



if __name__ == '__main__':
    res = longest_string_array(["abc", "cba", "def", "gha", "gi"])
    print(res)