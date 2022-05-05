from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '?' not in p and '*' not in p:
            return s == p
        # remove duplicate wildcards
        p = p[0]+''.join([p[i] for i in range(1, len(p)) if not (p[i] == p[i-1] == '*')])
        
        #print(p)
        #return False
        
        @lru_cache(maxsize=None)
        def dp(i_s, i_p):
            #print(i_s,i_p)
            # proceed through any easy matches
            while i_p < len(p) and i_s < len(s) and (p[i_p] == '?' or s[i_s] == p[i_p]):
                i_p += 1
                i_s += 1
                
            # if we have reached the end
            if i_p == len(p) or i_s == len(s):
                return (i_p == len(p) or (i_p == len(p)-1 and p[i_p] == '*')) and i_s == len(s)
        
            # work on a wild_card
            if p[i_p] == '*':
                return dp(i_s, i_p+1) or dp(i_s+1, i_p)
        
            # found a mismatch
            if s[i_s] != p[i_p]:
                return False

        return dp(0,0)
