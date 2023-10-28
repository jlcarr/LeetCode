from functools import cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulus = 10**9 + 7
        @cache
        def rec(pos,prev):
            if pos == n:
                return 1
            if prev == 'a':
                return rec(pos+1, 'e')
            if prev == 'e':
                return (rec(pos+1, 'a') + rec(pos+1, 'i')) % modulus
            if prev == 'i':
                return sum(rec(pos+1, c) for c in 'aeou') % modulus
            if prev == 'o':
                return (rec(pos+1, 'i') + rec(pos+1, 'u')) % modulus
            if prev == 'u':
                return rec(pos+1, 'a')
            return sum(rec(pos+1, c) for c in 'aeiou') % modulus
        
        return rec(0, '')
