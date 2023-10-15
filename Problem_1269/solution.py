from functools import cache
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modv = 10**9 + 7
        @cache
        def dp(pos, rem):
            result = 0
            if pos == 0 and rem == 0:
                return 1
            # left
            if pos-1 >= 0:
                result = (result + dp(pos-1, rem-1)) % modv
            # right
            if pos+1 < arrLen and pos+1 <= rem-1:
                result = (result + dp(pos+1, rem-1)) % modv
            # same
            if pos <= rem-1:
                result = (result + dp(pos, rem-1)) % modv
            return result

        return dp(0, steps)
