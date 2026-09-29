class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            speed = (r + l) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / speed)
            
            if time <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        
        return res