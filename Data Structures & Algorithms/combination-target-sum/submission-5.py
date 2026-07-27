class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def search(i, cur):
            if i > len(nums) - 1:
                return
            if cur > target:
                return
            elif cur == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            search(i, cur + nums[i])
            subset.pop()
            search(i + 1, cur)

        search(0, 0)
        return res