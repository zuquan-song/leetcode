import bisect

class Bisect:
    def __init__(self):
        pass

    def firstIdx(self, array, target):
        l, r = 0, len(array) - 1
        while l < r:
            mid = l + (r - l) // 2
            if array[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if array[l] == target else -1

    def lastIdx(self, array, target):
        l, r = 0, len(array) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if array[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return l if array[l] == target else -1

    # 第一个大于等于该元素的index
    # The returned insertion point i partitions the array a into two halves
    # so that all(val < x for val in a[lo:i]) for the left side and all(val >= x for val in a[i:hi]) for the right side.
    def bisect_left(self, array, target):
        l, r = 0, len(array) - 1
        while l < r:
            mid = l + (r - l) // 2
            if array[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if array[l] >= target else len(array)

    # 第一个大于该元素的index
    # The returned insertion point i partitions the array a into two halves
    # so that all(val <= x for val in a[lo:i]) for the left side and all(val > x for val in a[i:hi]) for the right side.
    def bisect_right(self, array, target):
        l, r = 0, len(array) - 1
        while l < r:
            mid = l + (r - l) // 2
            if array[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l if array[l] > target else len(array)

    # 最后一个小于等于index
    def last_index(self, array, target):
        l, r = 0, len(array) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if array[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return l if array[l] <= target else -1

if __name__ == '__main__':
    bquery = Bisect()
    # print(bquery.firstIdx([1, 2, 2, 2, 4], 2))
    # print(bquery.firstIdx([1, 2, 2, 2, 4], 4))
    # print(bquery.firstIdx([1, 2, 2, 2, 4], 1))
    # print(bquery.firstIdx([1, 2, 2, 2, 4], 0))
    # print(bquery.lastIdx([1, 2, 2, 2, 4], 2))
    # print(bquery.lastIdx([1, 2, 2, 2, 4], 4))
    # print(bquery.lastIdx([1, 2, 2, 2, 4], 1))
    # print(bquery.lastIdx([1, 2, 2, 2, 4], 0))
    # print(bquery.bisect_left([1, 2, 2, 2, 4], 0), bisect.bisect_left([1, 2, 2, 2, 4], 0))
    # print(bquery.bisect_left([1, 2, 2, 2, 4], 1), bisect.bisect_left([1, 2, 2, 2, 4], 1))
    # print(bquery.bisect_left([1, 2, 2, 2, 4], 2), bisect.bisect_left([1, 2, 2, 2, 4], 2))
    # print(bquery.bisect_left([1, 2, 2, 2, 4], 3), bisect.bisect_left([1, 2, 2, 2, 4], 3))
    # print(bquery.bisect_left([1, 2, 2, 2, 4], 4), bisect.bisect_left([1, 2, 2, 2, 4], 4))
    # print(bquery.bisect_left([1, 2, 2, 2, 4], 6), bisect.bisect_left([1, 2, 2, 2, 4], 6))

    print(bquery.bisect_right([1, 2, 2, 2, 4], 0), bisect.bisect_right([1, 2, 2, 2, 4], 0))
    print(bquery.bisect_right([1, 2, 2, 2, 4], 1), bisect.bisect_right([1, 2, 2, 2, 4], 1))
    print(bquery.bisect_right([1, 2, 2, 2, 4], 2), bisect.bisect_right([1, 2, 2, 2, 4], 2))
    print(bquery.bisect_right([1, 2, 2, 2, 4], 3), bisect.bisect_right([1, 2, 2, 2, 4], 3))
    print(bquery.bisect_right([1, 2, 2, 2, 4], 4), bisect.bisect_right([1, 2, 2, 2, 4], 4))
    print(bquery.bisect_right([1, 2, 2, 2, 4], 6), bisect.bisect_right([1, 2, 2, 2, 4], 6))