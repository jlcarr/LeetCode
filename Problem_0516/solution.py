from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def rec(i,j):
            if i == j:
                return 1
            if i+1 == j:
                return 1 + int(s[i] == s[j])
            if s[i] == s[j]:
                return 2 + rec(i+1,j-1)
            return max(rec(i+1,j), rec(i,j-1))

        return rec(0,n-1)
