from functools import cache
import math
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        modulo = 10**9 + 7
        @cache
        def rec(n, goal):
            result = 1
            # All playlists without at-least-once restriction 
            for i in range(k):
                result *= n - i
                result %= modulo
            for i in range(k,goal):
                result *= n - k
                result %= modulo
            # remove all playlists with fewer songs
            for i in range(n):
                result -= math.comb(n,i) * rec(i, goal) % modulo
                result %= modulo
            # finishing touch
            return (result + modulo) % modulo
        
        return rec(n, goal)
