def rotate(matrix, k):
  k = k % 4
  n = len(matrix)
  for _ in range(k):
    for i in range(n//2):
      for j in range(i + 1, n - i - 1):
        # n = 10
        #            i, j
        # [2, 1] => [1, 2] => [2,8] => [8, 2] => [2, 1]
        matrix[i][j] = matrix[j][i]
        matrix[][] = matrix[i][j]
        matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][j], matrix[n - j - 1][i] = matrix[j][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][j]

  return matrix


res = rotate([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]], 1)
for row in res:
	print(row)
