class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        i = 0
        ans = []
        while i < len(nums) and nums[i] < 1:
            if i > 0 and nums[i] == nums[i - 1]:
                print(i)
                i += 1
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        print(nums[j])
                        j += 1
                    k -= 1
            i += 1

        return ans