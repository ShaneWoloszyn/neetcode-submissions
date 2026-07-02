class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def search(arr):
            if False not in arr:
                res.append(subset.copy())
            for i, tf in enumerate(arr):
                if not tf:
                    arr[i] = True
                    subset.append(nums[i])
                    search(arr)
                    subset.pop()
                    arr[i] = False
        
        search([False] * len(nums))
        return res