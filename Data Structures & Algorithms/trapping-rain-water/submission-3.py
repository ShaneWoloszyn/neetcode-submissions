class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = list(accumulate(height, max))
        maxRight = list(accumulate(height[::-1], max))[::-1]
        res = 0
        for i in range(len(height)):
            if min(maxLeft[i], maxRight[i]) > height[i]:
                res += min(maxLeft[i], maxRight[i]) - height[i]

        return res