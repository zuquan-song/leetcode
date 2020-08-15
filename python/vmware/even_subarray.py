
def even_subarray(array, k):
    res = []
    n = len(array)
    for i in range(n):
        odd = 0
        for j in range(i, n):
            if array[j] % 2:
                odd += 1
            if odd <= k:
                res.append(array[i:j+1])
    return res

print(even_subarray([1,2,3,4], 1))
print(even_subarray([6,3,5,8], 1))
