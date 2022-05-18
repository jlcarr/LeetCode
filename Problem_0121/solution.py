class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        prev_low = prices[0]
        prev_high = prices[0]
        for p in prices:
            if p < prev_low:
                result = max(result, prev_high - prev_low)
                prev_low, prev_high = p,p
            elif p > prev_high:
                prev_high = p
        result = max(result, prev_high - prev_low)
        return result
