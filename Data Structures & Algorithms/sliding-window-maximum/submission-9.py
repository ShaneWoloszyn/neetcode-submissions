class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic decreasing stack
        # if we find a higher value, pop until a higher one
        # if its bigger than k we pop from the left until it fits

        # pair [val, i]
        cur = deque([])

        res = []

        for i in range(len(nums)):
            while cur and cur[-1][0] < nums[i]:
                cur.pop()

            while cur and i - cur[0][1] >= k:
                cur.popleft()
            
            
            cur.append([nums[i], i])

            if i >= k - 1:
                res.append(cur[0][0])
        
        return res