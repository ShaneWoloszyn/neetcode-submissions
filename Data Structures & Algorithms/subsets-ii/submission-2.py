class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []

        nums.sort()
        def search(i):
            if i == len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[i])
            search(i + 1)
            subset.pop()
            search(i + 1)
        
        search(0)

        return list(val for val in res)