class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        def getSquareDigits(n):
            res = []
            while n != 0:
                res.append((n % 10) ** 2)
                n = n // 10
            return sum(res)
        
        while n != 1:
            if n in seen:
                return False
            seen[n] = 1
            n = getSquareDigits(n)
            
        return True