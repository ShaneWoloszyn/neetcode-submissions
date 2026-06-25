class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 2 3 4 5
        #       l r
        # 0 0 0 1 0
        #     2 1 0
        #   
        first, second = 1, 0
        
        for i in range(n):
            temp = first
            first = first + second
            second = temp
        
        return first

