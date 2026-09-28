class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = []

        cur = 0
        for h in height:
            lMax.append(cur)
            cur = max(cur, h)
        

        res = 0
        cur = 0

        for i in range(len(height) - 1, -1, -1):
            res += min(cur, lMax[i]) - height[i] if min(cur, lMax[i]) - height[i] > 0 else 0
            cur = max(cur, height[i])
        
        return res