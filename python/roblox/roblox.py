def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Write your code here
    ub = [(unit, box) for unit, box in zip(unitsPerBox, boxes)]
    ub.sort(key=lambda x: (x[0], -x[1]))
    res = 0
    print(ub)
    while truckSize > 0:
        unit, box = ub.pop()
        print()
        if box <= truckSize:
            res += box * unit
            truckSize -= box
        else:
            res += truckSize * unit
            truckSize = 0
    return res

print(getMaxUnits([3,1,6], [2,7,4], 6))
print(getMaxUnits([6,5,2,7], [46335, 90039, 24796, 87808], 6))