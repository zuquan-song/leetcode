

def get_monotonic(arr):

    n = len(arr)
    res = 0
    for i in range(1, n - 1):
        if (arr[i-1] < arr[i] < arr[i+1]) or (arr[i-1] > arr[i] > arr[i+1]):
            res += 1

    return res

print(get_monotonic([1, 2, 1, -4, 5, 10]))