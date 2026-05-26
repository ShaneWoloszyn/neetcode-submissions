class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check midpoint
        # if higher than target, move r to mid
        # if less move l to mid
        # mid of r and l
        # once their == if its not -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

