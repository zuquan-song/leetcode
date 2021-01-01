
def box_drop(matrix):
    row, col = len(matrix), len(matrix[0])
    box = [['.'] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            box[j][row - 1 - i] = matrix[i][j]

    for i in range(col-1, -1, -1):
        for j in range(row):
            if box[i][j] == '#':
                k = i + 1
                while k < col and box[k][j] == '.':
                    k += 1
                box[i][j] = '.'
                box[k-1][j] = '#'

    return box


if __name__ == '__main__':
    box = ["*....*",
           "......",
           "..#*..",
           "..#...",
           "..#..."]
    box = box_drop(box)
    print(box)