class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nMap = set(nums)
        res = 0

        for n in nMap:
            if n - 1 in nMap:
                continue
            
            i = 1
            while n + i in nMap:
                i += 1
            
            res = max(res, i)
        
        return res