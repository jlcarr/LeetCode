class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit_with = -prices[0]
        profit_without = 0
        for price in prices:
            profit_with = max(profit_with, profit_without-price)
            profit_without = max(profit_without, profit_with+price-fee)
        return max(profit_with,profit_without)
