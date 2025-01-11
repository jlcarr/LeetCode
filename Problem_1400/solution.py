from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c = Counter(s)
        minv, maxv = 0,0
        for v in c.values():
            minv += v % 2
            maxv += v
        return minv <= k <= maxv

