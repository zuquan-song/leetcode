

class BringTop:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.storage = {}

    def draw(self):
        grid = [['O'] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if (i, j) in self.storage:
                    grid[self.n - j - 1][i] = self.storage[(i, j)][2]

        return "\n".join([" ".join(row) for row in grid])

    def overlap(self, bottomLeft, topRight, inputChar):
        bx, by = bottomLeft
        tx, ty = topRight

        for i in range(bx, tx + 1):
            for j in range(by, ty + 1):
                self.storage[(i, j)] = (bottomLeft, topRight, inputChar)

    def createShape(self, bottomLeft, topRight, inputChar):
        self.overlap(bottomLeft, topRight, inputChar)
        return self.draw()

    def bringTop(self, location):
        if location not in self.storage:
            self.draw()
        bottomLeft, topRight, inputChar = self.storage[(location[0], location[1])]
        self.overlap(bottomLeft, topRight, inputChar)
        return self.draw()

if __name__ == '__main__':
    bt = BringTop(5, 5)
    print(bt.createShape(bottomLeft=(2,2), topRight=(4,4), inputChar='a'))
    print()
    print(bt.createShape(bottomLeft=(1,1), topRight=(3,2), inputChar='b'))
    print()
    print(bt.bringTop(location=(4,2)))
