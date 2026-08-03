class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def search(seen):
            if not False in seen:
                res.append(subset.copy())
                return
            
            for i, tf in enumerate(seen):
                if not tf:
                    subset.append(nums[i])
                    seen[i] = True
                    search(seen)
                    subset.pop()
                    seen[i] = False
        
        search([False for _ in range(len(nums))])
        return res