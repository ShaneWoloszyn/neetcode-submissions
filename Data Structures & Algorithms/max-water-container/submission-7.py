class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1

        l = 0

        while l < len(heights):
            r = l + 1
            while r < len(heights):
                res = max(res, min(heights[l], heights[r]) * (r - l))
                r += 1
            l += 1
        
        return res