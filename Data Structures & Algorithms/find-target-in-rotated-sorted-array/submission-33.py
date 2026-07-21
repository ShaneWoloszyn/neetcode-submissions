class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            # if left is sorted
            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    # search left
                    r = m - 1
                else:
                    # search right
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        
        return -1