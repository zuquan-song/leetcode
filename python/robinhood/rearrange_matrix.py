import collections


class Test:
    def rearrange(self, matrix):

        counter = collections.defaultdict(int)
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                counter[v] += 1

        rev_counter = collections.defaultdict(list)
        for k, v in counter.items():
            rev_counter[v].append(k)


        res = []
        freqs = sorted(list(rev_counter.keys()))
        for key in freqs:
            values = sorted(rev_counter[key])
            for value in values:
                res.extend([value] * key)

        idx, n = 0, len(matrix)
        for k in range(n-1, -1, -1):
            i, j = n-1, k
            while j < n:
                matrix[i][j] = res[idx]
                idx += 1
                i, j = i - 1, j + 1

        for k in range(n-2, -1, -1):
            i, j = k, 0
            while i >= 0:
                matrix[i][j] = res[idx]
                idx += 1
                i, j = i - 1, j + 1
        return matrix


if __name__ == '__main__':
    t = Test()
    for row in t.rearrange([[1,3,3], [4,5,6], [7,7,9]]):
        print(row)



