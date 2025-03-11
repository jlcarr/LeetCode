from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        j = 0
        counts = Counter()
        result = 0
        for i,c in enumerate(s):
            counts[c] += 1
            while j < i and counts[s[j]] > 1:
                counts[s[j]] -= 1
                j += 1
            if sum(v > 0 for v in counts.values()) == 3:
                result += j + 1
        return result
