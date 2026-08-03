class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def search(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            search(i + 1)
            subset.pop()
            search(i + 1)
        
        search(0)

        return res