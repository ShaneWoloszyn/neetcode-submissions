class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]

        while len(dp) <= n:
            dp.append(dp[-1] + dp[-2])
        
        return dp[n]