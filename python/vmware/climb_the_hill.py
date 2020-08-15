import heapq


def climb_the_hill(nums):
    return min(non_xxcreasing_array(nums, lambda x: x, lambda x, y: x < y),
               non_xxcreasing_array(nums, lambda x: -x, lambda x, y: x > y))


def non_xxcreasing_array(nums, fn, cmp):
    hills, n, sm = [], len(nums), 0
    for i in range(n):
        if len(hills) and cmp(fn(hills[0]), nums[i]):
            dif = abs(fn(hills[0]) - nums[i])
            sm += dif
            heapq.heappop(hills)
            heapq.heappush(hills, fn(nums[i]))
        heapq.heappush(hills, fn(nums[i]))
    return sm

if __name__ == '__main__':
    nums1 = [0, 1, 2, 5, 6, 5, 7]
    nums2 = [9847, 3752, 5621, 7012, 1986, 3090, 1383, 6257, 9501, 7004, 6181, 9387, 9137, 9305, 7795, 9310,
			3904, 8328, 6656, 8123, 1796, 2754, 4372, 5200, 3893, 8568, 4436, 3973, 8498, 1879, 2731, 4651, 4388,
			453, 2465, 2669, 6384, 819, 8565, 1952, 7219, 4362, 3012, 9380, 2645, 4800, 2945, 5778, 1993, 1170,
			1356, 8557, 1497, 8921, 670, 5155, 9115, 1095, 9400, 9451, 9344, 4393, 4201, 8167, 8129, 2004, 8839,
			1457, 7682, 1881, 9266, 6366, 9889, 242, 5318, 5248, 3670, 7381, 6567, 2317, 2162, 6670, 5876, 1179,
			2482, 9270, 4326, 4166, 6122, 2016, 3008, 5349, 1723, 5816, 4030]
    print(climb_the_hill(nums1))
    print(climb_the_hill(nums2))
