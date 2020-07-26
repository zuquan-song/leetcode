
class Heap:
    def __init__(self, capacity):
        self.data = [0] * (capacity + 1)
        self.n = capacity
        self.count = 0

    def insert(self, data):
        if self.count >= self.n: return
        self.count += 1
        self.data[self.count] = data
        i = self.count
        while i >> 1 > 0 and self.data[i] > self.data[i >> 1]:
            self.data[i], self.data[i >> 1] = self.data[i >> 1], self.data[i]
            i = i >> 1

    def removeMax(self):
        if self.count == 0: return -1
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.heapify(1)

    def heapify(self, i):
        while True:
            maxPos = i
            if i * 2 <= self.n and self.data[i] < self.data[i << 1]:
                maxPos = i << 1
            if i * 2 + 1 <= self.n and self.data[maxPos] < self.data[i << 1 + 1]:
                maxPos = i << 1 + 1
            if maxPos == i:
                break
            self.data[i], self.data[maxPos] = self.data[maxPos]
            i = maxPos