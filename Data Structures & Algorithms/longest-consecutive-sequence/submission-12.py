class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nMap = Counter(nums)
        res = 0

        for key, frq in nMap.items():
            if key - 1 in nMap:
                continue
            i = 0
            while key + i in nMap:
                i += 1
                res = max(res, i)
        
        return res