

def zigzag(array):
    n = len(array)
    if n <= 2:
        return []
    res = []
    for i in range(n - 2):
        if (array[i] - array[i+1]) * (array[i+1] - array[i+2]) < 0:
            res.append(1)
        else:
            res.append(0)
    return res

print(zigzag([1, 2, 1, 3, 4]))