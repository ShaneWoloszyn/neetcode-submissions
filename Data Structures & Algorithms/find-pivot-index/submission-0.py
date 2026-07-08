class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0 for _ in range(len(nums))]
        cur = 0
        for i in range(len(nums)):
            leftSum[i] = cur
            cur += nums[i]
        
        rightSum = [0 for _ in range(len(nums))]
        cur = 0
        for i in range(len(nums) - 1, -1, -1):
            rightSum[i] = cur
            cur += nums[i]
        
        for i in range(len(nums)):
            if rightSum[i] == leftSum[i]:
                return i
        return -1