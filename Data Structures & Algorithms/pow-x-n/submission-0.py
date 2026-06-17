class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        if n > 0:
            ans = x
            for i in range(n - 1):
                ans *= x
        else:
            ans = 1
            for i in range(-n):
                ans /= x
        
        return ans