class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nMap = {}

        for n in nums:
            nMap[n] = 1
        
        maxLen = 0
        cur = 0
        for key, tok in nMap.items():
            cur = 0
            i = 1
            while key + i in nMap:
                cur += 1
                i += 1
            maxLen = max(cur, maxLen)
        return maxLen + 1