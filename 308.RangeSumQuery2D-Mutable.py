class NumMatrix:

    def __init__(self, matrix):
        self.mat = []
        for i in range(len(matrix)):
            self.mat.append([0])
            for j in range(len(matrix[0])):
                self.mat[-1].append(self.mat[-1][-1] + matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        originVal = self.mat[row][col + 1] - self.mat[row][col]
        diff = val - originVal
        for j in range(col + 1, len(self.mat[row])):
            self.mat[row][j] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            res += self.mat[i][col2 + 1] - self.mat[i][col1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)