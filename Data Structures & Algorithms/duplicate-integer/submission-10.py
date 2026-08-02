class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nMap = Counter(nums)

        for key, frq in nMap.items():
            if frq > 1:
                return True
        
        return False