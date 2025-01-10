from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal = Counter()
        for b in words2:
            universal |= Counter(b)

        return [a for a in words1 if universal <= Counter(a)]

