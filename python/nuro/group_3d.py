import heapq
import collections

class UnionFind:

    def __init__(self, n):
        self.group = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        t1 = i
        while self.group[t1] != t1:
            t1 = self.group[t1]

        while i != t1:
            i, self.group[i] = self.group[i], t1
        return t1

    def union(self, i, j):
        t1 = self.find(i)
        t2 = self.find(j)
        if self.rank[t1] > self.rank[t2]:
            self.group[t2] = t1
        else:
            self.group[t1] = t2
        if self.rank[t1] == self.rank[t2]:
            self.rank[t2] += 1


def group(points, k):
    dist = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2] - b[2])
    n, hq = len(points), []
    for i in range(n):
        for j in range(i+1, n):
            hq.append((dist(points[i], points[j]), i, j))
    heapq.heapify(hq)

    uf = UnionFind(n)
    while len(hq):
        distance, i, j = heapq.heappop(hq)
        if distance > k:
            break

        if uf.find(i) != uf.find(j):
            uf.union(i, j)

    groups = collections.defaultdict(list)

    for i, point in enumerate(points):
        groups[uf.find(i)].append(point)

    return groups.values()

if __name__ == '__main__':
    print(group([(1,2,5), (1,2,4), (2,2,4), (4,2,4), (5,2,4), (5,3,2)], 5))
