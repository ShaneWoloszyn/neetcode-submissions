class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1

        maxProf = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                maxProf = max(maxProf, prof)
            else:
                l = r
            r += 1
        return maxProf