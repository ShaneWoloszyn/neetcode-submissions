class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nMap = set()
        

        for n in nums:
            if n in nMap:
                return True
            nMap.add(n)
        
        return False