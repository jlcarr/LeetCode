class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        result = 0
        prevcount = 0
        prev = None
        for c in s:
            if c != prev:
                prev = c
                prevcount = 0
            prevcount += 1
            result += prevcount
            result %= mod
        
        return result
