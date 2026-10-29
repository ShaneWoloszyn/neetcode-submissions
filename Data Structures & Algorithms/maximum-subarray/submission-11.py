class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = -float('inf')
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            res = max(res, cur)
            if cur < 0:
                cur = 0
        
        return res