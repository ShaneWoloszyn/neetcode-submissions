class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        subset = []
        def search(i):
            if i >= len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[i])
            search(i + 1)

            subset.pop()
            search(i + 1)

        search(0)
        ans = []
        for n in res:
            ans.append(n)
        return ans