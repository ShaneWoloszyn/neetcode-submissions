from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[l] and nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
            
        return res