class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = 1
        water = 0
        height = 0
        while l < len(heights):
            while r < len(heights):
                if heights[l] > heights[r]:
                    height = heights[r]
                else:
                    height = heights[l]
                if water < (height * (r - l)):
                    water = height * (r - l)
                r += 1
            l += 1
            r = l + 1
        return water