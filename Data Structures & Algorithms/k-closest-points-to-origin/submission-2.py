class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distMap = []

        for x, y in points:
            distMap.append([x ** 2 + y ** 2, x, y])
        
        heapq.heapify(distMap)

        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(distMap)
            res.append([x, y])

        return res