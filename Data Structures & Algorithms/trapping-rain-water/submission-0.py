class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        l = 0
        for h in height:
            maxLeft.append(l)
            l = max(h, l)
        r = 0
        maxRight = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = r
            r = max(height[i], r)
        
        tot = 0

        for i, h in enumerate(height):
            temp = min(maxRight[i], maxLeft[i]) - h
            if temp > 0:
                tot += temp
        
        return tot