class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                threeSum = nums[l] + nums[r] + n
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans
