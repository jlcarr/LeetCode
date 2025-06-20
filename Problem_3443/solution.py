class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        result = 0
        xp,xn, yp,yn = 0,0, 0,0
        for i,c in enumerate(s):
            if c == 'N':
                yp += 1
            if c == 'S':
                yn += 1
            if c == 'E':
                xp += 1
            if c == 'W':
                xn += 1
            result = max(result, 
                abs(xp-xn) + abs(yp-yn) + 
                2 * min(k, min(xp, xn) + min(yp, yn))
            )
        return result
