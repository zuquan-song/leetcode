from collections import Counter

def droppedRequest(requestTime):
    if not requestTime or len(requestTime) == 0:
        return 0

    rules = [[1, 3], [10, 20], [60, 60]]
    dropped = set()
    maximum = max(requestTime)
    dic = Counter(requestTime)

    presum = [0] * (maximum + 1)
    for i in range(1, maximum + 1):
        presum[i] = presum[i-1] + dic.get(i, 0)

    for rule in rules:
        window = min(rule[0], maximum)
        for i in range(maximum - window + 1):
            numRequest = presum[i + window] - presum[i]
            diff = max(0, numRequest - rule[1])
            for index in range(diff):
                endIndex = presum[i + window] - 1
                dropped.add(endIndex - index)

    return len(dropped)

RequestTime = [1,1,1,1,1,2,2,2,3,3,3,4,4,4,11,11,11,6,6,6,5,5,5]
print(droppedRequest(RequestTime))

RequestTime = [1,1,1,1,2]
print(droppedRequest(RequestTime))

RequestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,6,6,6,5,5,5,7,7]
print(droppedRequest(RequestTime))

RequestTime = [1,1,1,2,2,2,3,3,3,4,4,4,6,6,6,5,5,5,7,7,7,8,8,8,9,9,9]
print(droppedRequest(RequestTime))

RequestTime = [1,1,1,1,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9,10,10,11,11,11,11,11,11,12,12,12,12,12,12,12,13,13,13,13,14,14,14,14,14,16,16,16,16,16,16,17,17,17,18,18,18,18,18,18,18,18,19,19,19,19,19,19,19,20,20,20,20,20]
print(droppedRequest(RequestTime))