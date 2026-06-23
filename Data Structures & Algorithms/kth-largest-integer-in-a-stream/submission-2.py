class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = [n for n in nums]
        heapq.heapify(self.arr)
        self.maxL = k
        while len(self.arr) > k:
            heapq.heappop(self.arr)

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        while len(self.arr) > self.maxL:
            heapq.heappop(self.arr)
        return self.arr[0]
        
