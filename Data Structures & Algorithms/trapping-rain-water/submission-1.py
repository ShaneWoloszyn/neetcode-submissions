class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = []
        maxR = [0] * (len(height))

        area = 0

        cur = 0
        for h in height:
            cur = max(h, cur)
            maxL.append(cur)
        
        cur = 0
        for i in range(len(height) - 1, -1, -1):
            cur = max(height[i], cur)
            maxR[i] = cur
        
        for i, h in enumerate(height):
            cur = min(maxR[i], maxL[i]) - h
            if cur > 0:
                area += cur

        return area
            