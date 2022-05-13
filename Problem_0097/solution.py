from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if sorted(s1+s2) != sorted(s3):
            return False
        
        @cache
        def dp(i1, i2):
            if i1 == len(s1) and i2 == len(s2):
                return True
            if i1 < len(s1) and s1[i1] == s3[i1+i2] and dp(i1+1, i2):
                return True
            if i2 < len(s2) and s2[i2] == s3[i1+i2] and dp(i1, i2+1):
                return True
            return False
            
        return dp(0,0)
