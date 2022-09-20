from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = sorted(s)
        s = sorted(s, key= lambda x: c[x], reverse=True)
        return s
