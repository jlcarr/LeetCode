from collections import Counter
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        c = Counter([hash(word[i*k:(i+1)*k]) for i in range(n//k)])
        _,max_count = c.most_common(1)[0]
        return n//k - max_count
