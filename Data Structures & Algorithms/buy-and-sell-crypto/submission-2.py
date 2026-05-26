class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxProf = 0

        while r < len(prices):
            maxProf = max(maxProf, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r 
                r = r + 1
            else:
                r = r + 1
        return maxProf