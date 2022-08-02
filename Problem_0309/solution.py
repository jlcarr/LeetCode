from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i=0, has_stock=False):
            if i >= len(prices):
                return 0
            if has_stock:
                return max(dp(i+1, True), dp(i+2, False)+prices[i])
            else:
                return max(dp(i+1, False), dp(i+1, True)-prices[i])
        
        return dp()
            
