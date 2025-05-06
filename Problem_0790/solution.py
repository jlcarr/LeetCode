from functools import cache
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        @cache
        def rec(rem, state):
            # end of the line
            if rem <= 0:
                return rem == 0 and state == 0
            # empty
            if state == 0:
                return (rec(rem-1, 0) + \
                    rec(rem-2, 0) + \
                    rec(rem-1, 1) + \
                    rec(rem-1, 2)) % mod
            # upper
            elif state == 1:
                return (rec(rem-1, 2) + \
                    rec(rem-2, 0)) % mod
            # lower
            elif state == 2:
                return (rec(rem-1, 1) + \
                    rec(rem-2, 0)) % mod
        return rec(n, 0)
