
left = lambda x: (x + 1) * 2 - 1
right = lambda x: (x + 1) * 2
father = lambda x: (x-1)//2

def max_heapify(nums, i):
    l, r, n = left(i), right(i), len(nums)
    if l < n and nums[l] > nums[i]:
        largest = l
    else:
        largest = i
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        print(i, nums)
        max_heapify(nums, largest)

def build_max_heapify(nums):
    n = len(nums)
    for i in range(n//2, -1, -1):
        max_heapify(nums, i)
    return nums

def heap_extract_max(nums):
    max_val = nums[0]
    nums[0] = nums[len(nums) - 1]
    nums.pop()
    max_heapify(nums, 0)
    return max_val

def max_heap_insert(nums, value):
    nums.append(value)
    n = len(nums)
    cur = n - 1
    while cur > 0 and nums[father(cur)]:
        nums[cur], nums[father(cur)] = nums[father(cur)], nums[cur]
        cur = father(cur)

    return nums

nums = [12, 25, 7, 16, 23, 15, 8, 6, 19, 21, 11]
build_max_heapify(nums)
print(nums)
# heap_extract_max(nums)
# print(nums)
# max_heap_insert(nums, 56)
# print(nums)