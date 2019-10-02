import heapq

class Solution:
    def kClosest(self, points, K: int):
        def getDist(point):
            return - (point[0] ** 2 + point[1] ** 2)

        res = [(getDist(point), point) for point in points[:K]]

        heapq.heapify(res)
        print(res)
        for i in range(K, len(points)):
            if res[0][0] < getDist(points[i]):
                heapq.heappop(res)
                heapq.heappush(res, (getDist(points[i]), points[i]))
        return [val for _, val in res]