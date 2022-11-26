from functools import cache
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        self.s = s

        @cache
        def dp(i):
            if i == n:
                return -1
            result = n-i
            for j in range(i+1,n+1):
                if self.isPalindrome(i,j-1):
                    result = min(result, 1 + dp(j))
            return result
        return dp(0)

    @cache
    def isPalindrome(self,i,j):
        if j <= i:
            return True
        if self.s[i] == self.s[j]:
            return self.isPalindrome(i+1, j-1)

