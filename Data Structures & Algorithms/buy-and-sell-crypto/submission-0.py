class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max = 0
        while l < len(prices) - 1:
            while (r < len(prices) and prices[r] - prices[l] > 0):
                if (prices[r] - prices[l] > max):
                    max = prices[r] - prices[l]
                r = r + 1
            l = l + 1
            r = l + 1
        return max