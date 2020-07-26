
class SolutionSort(object):

    def __init__(self):
        pass

    def sort(self, array):
        length = max(array)
        counting = [0] * (length + 1)
        for num in array:
            counting[num] += 1

        for i in range(1, len(counting)):
            counting[i] += counting[i - 1]
        tmp = [0] * len(array)
        for num in array[::-1]:
            tmp[counting[num] - 1] = num
            counting[num] -= 1
        return tmp

if __name__ == '__main__':
    solu = SolutionSort()
    print(solu.sort([6,1,2,4,1,3]))
