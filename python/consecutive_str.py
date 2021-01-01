import heapq
def booleanDeque(n, operations):
    a = list(range(n))
    heapq.heapify(a)
    zeros = set(a)
    # print()
    # print(a, zeros)
    for oper in operations:
        if oper == "L":
            if len(a):
                i = heapq.heappop(a)
                zeros.remove(i)
        else:
            idx = int(oper[1:])
            if idx not in zeros:
                heapq.heappush(a, idx)
                zeros.add(idx)
        # print(oper, a, zeros)
    res = ["1"] * n
    for idx in a:
        res[idx] = "0"
    return res

print(booleanDeque(5, ["L", "L", "C1"]))
print(booleanDeque(5, ["L", "L", "C1", "C0", "C1"]))
print(booleanDeque(5, ["L", "L", "C0", "L", "C3"]))