class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-s for s in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            s1 = -heapq.heappop(arr)
            s2 = -heapq.heappop(arr)

            if abs(s1 - s2) != 0:
                heapq.heappush(arr, -abs(s1 - s2))

        
        return -arr[0] if len(arr) != 0 else 0