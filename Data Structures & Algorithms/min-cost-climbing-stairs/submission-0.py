class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost at n step is 0
        # cost at n - 1 is x
        # cost at n - 2 is x + y
        # cost at n - 3 is z + x or z + y
        
        arr = [-1 for i in range(len(cost) + 1)]
        i = len(arr) - 1

        arr[i] = 0
        i -= 1
        arr[i] = cost[i]
        i -= 1
        
        while i >= 0:
            arr[i] = cost[i] + min(arr[i + 1], arr[i + 2])
            i -= 1
        
        return min(arr[0], arr[1])