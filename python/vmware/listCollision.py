import heapq

def listCollision(arr):
    arr = [-val for val in arr]
    heapq.heapify(arr)
    while len(arr) > 1:
        print(arr)
        v1, v2 = heapq.heappop(arr), heapq.heappop(arr)
        if abs(v1 - v2) != 0:
            heapq.heappush(arr, -abs(v1 - v2))
    if len(arr) == 1:
        return -arr[0]
    return 0

print(listCollision([1, 4,5,6,7]))