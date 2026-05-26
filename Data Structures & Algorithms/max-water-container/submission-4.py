class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = 1

        maxVol = 0
        vol = 0

        while l < len(heights) - 1:
            vol = (r - l) * min(heights[r], heights[l])
            maxVol = max(maxVol, vol)
            r += 1
            if r > len(heights) - 1:
                l += 1
                r = l + 1
        return maxVol