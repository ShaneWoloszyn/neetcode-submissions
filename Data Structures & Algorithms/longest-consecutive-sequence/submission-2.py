class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        for i in range(len(nums)):
            cur = 1
            while nums[i] + cur in nums:
                cur += 1
            maxLen = max(cur, maxLen)
        return maxLen