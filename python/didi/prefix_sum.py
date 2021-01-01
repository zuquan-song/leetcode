

def prefix_sum(A, B):
    total_a, total_b = [0], [0]
    n = len(A)
    for val in A:
        total_a.append(val + total_a[-1])
    for val in B:
        total_b.append(val + total_b[-1])

    if total_b[-1] != total_a[-1] or total_a[-1] % 2 != 0:
        return 0
    desired_half = total_a[-1] // 2
    counter = 0
    for i in range(1, n):
        if total_a[i] == total_b[i] == desired_half:
            counter += 1
    return counter

print(prefix_sum([4,-1,0,3], [-2,5,0,3]))
print(prefix_sum([2,-2,-3,3], [0,0,4,-4]))
print(prefix_sum([4,-1,0,3], [-2,6,0,4]))
print(prefix_sum([0,0,0],[0,0,0]))
print(prefix_sum([3,2,6], [4,1,6]))
print(prefix_sum([1,4,2,-2,5], [7,-2,-2,2,5]))