class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while l < len(prices):
            while r < len(prices):
                if profit < (prices[r] - prices[l]):
                    profit = prices[r] - prices[l]
                r += 1
            l += 1
            r = l + 1
        return profit