class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        end = []
        l = 0
        r = k
        while r < len(nums) + 1:
            # find max of nums[l:r]
            maxN = -10e10
            for n in nums[l:r]:
                if n > maxN:
                    maxN = n
            end.append(maxN)
            l += 1
            r += 1
        return end