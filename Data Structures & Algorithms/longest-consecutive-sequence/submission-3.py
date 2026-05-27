class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        i = 0
        for n in nums:
            if n - 1 in nums:
                continue
            else:
                i = n
                while i in nums:
                    i += 1
                maxLen = max(maxLen, (i - n))
        return maxLen