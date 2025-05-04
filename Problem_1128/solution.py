from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum(c*(c-1)//2 for c in Counter(map(tuple, map(sorted, dominoes))).values())
