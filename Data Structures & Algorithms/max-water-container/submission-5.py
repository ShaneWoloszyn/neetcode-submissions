class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxVol = 0
        while l < r:
            vol = (r - l) * min(heights[r], heights[l])
            maxVol = max(vol, maxVol)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return maxVol