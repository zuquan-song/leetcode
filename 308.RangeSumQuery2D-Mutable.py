class NumMatrix:

    def __init__(self, matrix):
        if not len(matrix) or not len(matrix[0]):
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.nums = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        if not self.m or not self.n:
            return
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def sum(row, col):
            res = 0
            i = row
            while i > 0:
                j = col
                while j > 0:
                    res += self.tree[i][j]
                    j -= j & (-j)
                i -= i & (-i)
            return res

        if not self.m or not self.n:
            return 0
        return sum(row2 + 1, col2 + 1) + sum(row1, col1) - sum(row1, col2 + 1) - sum(row2 + 1, col1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)