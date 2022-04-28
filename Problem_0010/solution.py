from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache()
        def dp(i_s, i_p):
            #print(i_s, i_p)
            if i_s == len(s) and i_p == len(p):
                return True
            elif i_p == len(p):
                return False
            
            if i_p + 1 < len(p) and p[i_p+1] == '*': # is there a *
                if i_s < len(s) and (s[i_s] == p[i_p] or p[i_p] == '.'):
                    if dp(i_s+1, i_p):
                        return True
                    if dp(i_s+1, i_p+2):
                        return True
                #print("dp 1")
                return dp(i_s, i_p+2)
            else:
                if i_s == len(s):
                    return False
                if s[i_s] != p[i_p] and p[i_p] != '.':
                    return False
                #print("dp 2")
                return dp(i_s+1, i_p+1)
        return dp(0, 0)
