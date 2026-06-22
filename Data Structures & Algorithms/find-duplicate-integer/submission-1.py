class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                return i + 1
            nums[i] *= -1
        return -1