class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def search(seen):
            if not False in seen:
                res.append(subset.copy())
                return
                        
            for i in range(len(nums)):
                if not seen[i]:
                    subset.append(nums[i])
                    seen[i] = True
                    search(seen)
                    seen[i] = False
                    subset.pop()
        
        search([False] * len(nums))

        return res