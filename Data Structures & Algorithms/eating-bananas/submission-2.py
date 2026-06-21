class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float('inf')

        while l <= r:
            m = (l + r) // 2
            print(m)
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / m)
            
            if hrs <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans