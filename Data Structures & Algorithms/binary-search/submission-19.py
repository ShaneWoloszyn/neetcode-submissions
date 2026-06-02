class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            print(nums[m])
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m
            else:
                return m
        return l if (l < len(nums) and nums[l] == target) else -1