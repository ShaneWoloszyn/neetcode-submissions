class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        maxL = []
        cur = 0
        for h in height:
            maxL.append(cur)
            cur = max(cur, h)

        maxR = []
        cur = 0
        for h in height[::-1]:
            maxR.append(cur)
            cur = max(cur, h)
        maxR = maxR[::-1]
        
        for i, h in enumerate(height):
            volume = min(maxR[i], maxL[i]) - h
            if volume > 0:
                res += volume
        
        return res