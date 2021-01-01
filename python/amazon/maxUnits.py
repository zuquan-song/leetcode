import heapq

def maxUnits(num, boxes, unitSize, unitsPerBox, truckSize):
    hp = list(zip([-sz for sz in unitsPerBox], boxes))
    heapq.heapify(hp)
    res = 0
    while truckSize > 0 and len(hp) > 0:
        units, box_num = heapq.heappop(hp)
        real_boxes = min(truckSize, box_num)
        res += -1 * units * real_boxes
        truckSize -= real_boxes
    return res

print(maxUnits(3, [1, 2, 3], 3, [3, 2, 1], 3))
print(maxUnits(3, [2,5,3], 3, [3,2,1], 50))
