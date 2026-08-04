class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr)

        for i, point in enumerate(points):
            x, y = point
            heapq.heappush(arr, (-((x ** 2 + y ** 2) ** 0.5), i))
        
        print(arr)
        while len(arr) > k:
            heapq.heappop(arr)
        
        print(arr)
        res = []
        while len(arr) != 0:
            dist, i = heapq.heappop(arr)
            res.append(points[i])
        
        return res