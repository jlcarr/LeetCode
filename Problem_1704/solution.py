class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        l = [s[i].lower() in 'aeiou' for i in range(n)]
        r = [s[i+n].lower() in 'aeiou' for i in range(n)]
        return sum(l) == sum(r)
