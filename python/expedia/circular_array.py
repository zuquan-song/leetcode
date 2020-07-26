
class Solution():
    def circularArray(self, m, n, dests):
        start = []
        end = []
        for i in range(len(dests) - 1):
            if dests[i] > dests[i + 1]:
                start.extend([dests[i], 0])
                end.extend([dests[i+1], m])
            else:
                start.append(dests[i])
                end.append(dests[i+1])

        start.sort()
        end.sort()
        startPtr, endPtr = 0, 0
        counter = 0
        result = 0
        maxCnt = 0
        while startPtr < len(start):
            if start[startPtr] > end[endPtr]:
                counter -= 1
                endPtr += 1
            counter += 1
            if counter > maxCnt:
                maxCnt, result = counter, start[startPtr]
            startPtr += 1

        return result

if __name__ == '__main__':
    solu = Solution()
    print(solu.circularArray(10, 4, [1, 5, 10, 5]))
    print(solu.circularArray(5, 2, [1, 5]))