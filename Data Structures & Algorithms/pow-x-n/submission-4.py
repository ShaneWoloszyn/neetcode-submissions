class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        rev = n < 0
        n = abs(n)
        mult = x
        while n > 1:
            x = x * mult
            n -= 1
        
        return 1/x if rev else x