class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def search(pick: List[bool]):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    search(pick)
                    subset.pop()
                    pick[i] = False
        
        search([False] * len(nums))
        return res