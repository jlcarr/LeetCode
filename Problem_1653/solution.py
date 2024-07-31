class Solution:
    def minimumDeletions(self, s: str) -> int:
        atot = s.count('a')
        btot = len(s) - atot
        result = atot
        bcount = 0
        for i,c in enumerate(s):
            bcount += c == 'b'
            result = min(result, (bcount)+(atot - (i+1-bcount)))
        return result
