class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        dists = []

        for x, y in points:
            dist = math.sqrt((x * x) + (y * y))
            dists.append([dist, x, y])
        
        heapq.heapify(dists)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(dists)
            res.append([x, y])
            k -= 1
        return res