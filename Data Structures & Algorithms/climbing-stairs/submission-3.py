class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        i = 1
        while len(dp) < n + 1:
            dp.append(dp[i - 1] + dp[i])
            i += 1
        
        return dp[n]