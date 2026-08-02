class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nMap = {}
        for n in nums:
            nMap[n] = 1
        
        res = 0
        for n in nums:
            if n - 1 in nMap:
                continue
            i = 1
            while n + i in nMap:
                i += 1
            res = max(res, (i))

        return res