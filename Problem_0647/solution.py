class Solution:
    def countSubstrings(self, s: str) -> int:
        cache = dict()
        def dp(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i] != s[j]:
                dp(i+1,j)
                dp(i,j-1)
                cache[(i,j)] = False
            elif j-i <= 1 or dp(i+1,j-1):
                cache[(i,j)] = True
            else:
                cache[(i,j)] = False
            return cache[(i,j)]
        for i in range(len(s)):
            for j in range(i,len(s)):
                dp(i, j)
        #print(cache)
        return sum(cache.values())
        
