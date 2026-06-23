class Solution:
    def myPow(self, x: float, n: int) -> float:
        tot = 1
        i = n

        if i < 0:
            i = abs(i)
        
        while i:
            tot *= x
            i -= 1

        if n < 0:
            return 1/tot
        return tot
