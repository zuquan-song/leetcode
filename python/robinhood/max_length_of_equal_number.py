

def max_length(arr):
    n = len(arr)

    counter = 0
    memo = {0:-1}
    mx, rg = 0, None
    for i in range(n):
        if arr[i] == 1:
            counter += 1
        else:
            counter -= 1

        if counter not in memo:
            memo[counter] = i
        else:
            if mx < i - memo[counter]:
                mx = max(mx, i - memo[counter])
                rg = (memo[counter]+1, i)

    return rg

print(max_length([1, 0, 0, 1, 0, 1, 1]  ))

