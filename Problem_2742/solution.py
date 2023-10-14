from functools import cache
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        s = sum(cost)
        @cache
        def dp(i, rem):
            if rem <= 0:
                return 0
            if i == n:
                if rem > 0:
                    return s
                return 0
            result = cost[i] + dp(i+1, rem-1-time[i])
            result = min(result, dp(i+1, rem))
            return result

        return dp(0, n)
