
def smallerThan(keys, x):

    i = 0
    n = len(keys)
    for j in range(n):
        if keys[j] <= x:
            keys[i], keys[j] = keys[j], keys[i]
            i += 1
    return keys[:i]


print(smallerThan([1, 3, 5, 7, 9, 11], 5))