from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i < len(s) and s[i] == '0':
                return 0
            if i == len(s)-1 or i == len(s):
                return 1
            result = dp(i+1)
            if int(s[i:i+2]) <= 26:
                result += dp(i+2)
            return result
        return dp(0)
