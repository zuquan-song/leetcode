

class Cuckoo:

    def __init__(self):
        self.table_size = 41
        self.table = [[-1] * 2 for i in range(self.table_size)]
        self.r = 0
        self.keys = []

    def hash(self, key, next):
        if next == 0:
            return (key + self.r) % self.table_size
        else:
            return ((key + self.r) // self.table_size) % self.table_size

    def put(self, key):
        count = 1
        cur_key = key
        actual_key = key
        next = 0
        f = 0
        while True:
            if not next:
                index = self.hash(cur_key, next)
                cur_key, self.table[index][0] = self.table[index][0], cur_key
                next = 1
            else:
                index = self.hash(cur_key, next)
                cur_key, self.table[index][1] = self.table[index][1], cur_key
                next = 0

            if cur_key == -1:
                break

            if actual_key == cur_key:
                count += 1

            if count >= 3:
                f = 1
                break

        return f

    def rehash(self):
        self.r += 2
        self.table = [[-1] * 2 for _ in range(self.table_size)]
        for i in range(0, len(self.keys)):
            f = self.put(self.keys[i])
            if f == 1:
                self.rehash()


a, b = [], []
c = Cuckoo()
nums = [1,2,3,4,5,10,20,43,50,60,72,94,99,42]
for num in nums:
    c.keys.append(num)
    value = c.put(num)
    if value == 1:
        c.rehash()
for row in c.table:
    print(row)