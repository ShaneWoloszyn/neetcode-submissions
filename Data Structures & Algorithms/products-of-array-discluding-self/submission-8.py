class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lSum = []

        cur = 1
        for n in nums:
            lSum.append(cur)
            cur *= n
        
        cur = 1
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            res[i] = cur * lSum[i]
            cur *= nums[i]
        
        return res
        
