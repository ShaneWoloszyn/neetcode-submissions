class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = []
        cur = 0
        for h in height:
            lMax.append(cur)
            cur = max(cur, h)
        
        rMax = [0 for _ in range(len(height))]
        cur = 0
        for i in range(len(height) - 1, -1, -1):
            rMax[i] = cur
            cur = max(cur, height[i])
        
        res = 0

        for i in range(len(height)):
            if height[i] < min(lMax[i], rMax[i]):
                res += min(lMax[i], rMax[i]) - height[i]
        
        return res