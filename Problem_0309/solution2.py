class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty_max, holding_max, cooling_down_max = 0,-prices[0],0
        for n in prices:
            empty_max, holding_max, cooling_down_max = \
                max(empty_max, cooling_down_max), \
                max(empty_max-n, holding_max), \
                holding_max+n
            
        return max(empty_max, holding_max, cooling_down_max)
            
