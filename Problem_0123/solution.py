class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # get max sell-off price from future going backwards
        # compute max last transaction profits from this running through backwards
        # So far linear
        # Then we can run backwards one last time keeping track of future value and future profit
        
        profit = [0] * len(prices)
        
        max_future_price = prices[-1]
        max_future_profit = 0
        for i in range(len(prices)-2, -1, -1):
            max_future_price = max(max_future_price, prices[i+1])
            max_future_profit = max(max_future_profit, max_future_price - prices[i])
            profit[i] = max_future_profit
            
        min_past_price = prices[0]
        for i in range(len(prices)):
            min_past_price = min(min_past_price, prices[i])
            profit[i] += prices[i] - min_past_price

        return max(profit)
        
        
