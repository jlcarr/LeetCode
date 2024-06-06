from collections import Counter
from functools import reduce
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return list(reduce(lambda x,y: x&y, map(Counter,words)).elements())
