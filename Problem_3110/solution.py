from itertools import pairwise
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum([abs(i-j) for i,j in pairwise(map(ord,s))])
