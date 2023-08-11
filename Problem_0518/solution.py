from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        coins.sort(reverse=True)
        @cache
        def dp(amount, i):
            result = 0
            if i + 1 < len(coins):
                result += dp(amount, i+1)
            # use the coin (again)
            diff = amount - coins[i]
            if diff > 0:
                result += dp(diff, i)
            elif diff == 0:
                result += 1
            return result
        return dp(amount, 0)
