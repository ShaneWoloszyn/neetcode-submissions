class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nMap = {}

        for n in nums:
            if n in nMap:
                return True
            nMap[n] = 1
        
        return False