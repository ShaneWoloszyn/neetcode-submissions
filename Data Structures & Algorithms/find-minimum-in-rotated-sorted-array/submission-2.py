class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            m = (l + r) //2

            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
            res = min(res, nums[m])
        
        return res