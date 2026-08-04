class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minStack = nums
        heapq.heapify(self.minStack)

        while len(self.minStack) > k:
            heapq.heappop(self.minStack)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.minStack, val)
        if len(self.minStack) > self.k:
            heapq.heappop(self.minStack)
        
        return self.minStack[0]