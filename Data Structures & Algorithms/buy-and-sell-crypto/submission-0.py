class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = max(price-lowest, profit)
        return profit