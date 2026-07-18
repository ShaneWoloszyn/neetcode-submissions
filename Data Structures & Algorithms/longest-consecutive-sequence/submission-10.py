class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            cur = 1
            if n - 1 in nums:
                continue
            
            while n + cur in nums:
                cur += 1
            
            res = max(cur, res)
        
        return res