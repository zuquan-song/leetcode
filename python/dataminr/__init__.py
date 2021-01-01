from heapq import *

def max_height(N, buildings, heights):

    hp = [(0,0,1)]
    built = {}
    built[1] = 0

    for b, h in zip(buildings, heights):
        hp.append((h, 0, b))
        built[b] = h
    heapify(hp)

    while hp:
        h, seq, b = heappop(hp)
        if b-1 > 0:
            if b-1 not in built or (b-1 in built and built[b-1] > h+1):
                built[b-1] = h+1
                heappush(hp, (h+1, seq+1, b-1))
        if b+1 <= N:
            if b+1 not in built or (b+1 in built and built[b+1] > h+1):
                built[b+1] = h+1
                heappush(hp, (h + 1, seq + 1, b + 1))
    print(sorted(list(zip(built.keys(), built.values()))))
    return max(built.values())

print(max_height(10, [4,5,6], [100,2,1]))
