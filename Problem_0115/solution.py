from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(i_s,i_t):
            #finished
            if i_s == len(s) or i_t == len(t):
                if i_t != len(t):
                    return 0
                else:
                    return 1
            result = 0
            if s[i_s] == t[i_t]:
                result += dp(i_s+1, i_t+1)
            result += dp(i_s+1,i_t)
            return result
        
        return dp(0,0)
