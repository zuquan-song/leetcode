import collections
import heapq

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if self.size[ra] <= self.size[rb]:
            self.parent[ra] = rb
            self.size[rb] += self.size[ra]
        elif self.size[ra] > self.size[rb]:
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]


def listOfGroups(dots, k):
    distance = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])
    n = len(dots)
    heap = []
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i):
            if distance(dots[i], dots[j]) <= k and uf.find(i) != uf.find(j):
                uf.union(i, j)

    groups = collections.defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(dots[i])
    return list(groups.values())


import random

data = []
for i in range(100):
    data.append((random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))
groups = listOfGroups(data, 20)
for group in groups:
    print(group)
