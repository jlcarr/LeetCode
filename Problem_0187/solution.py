from collections import deque, Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = Counter()
        i = 10
        while i <= len(s):
            counts[s[i-10:i]] += 1
            i += 1
        
        return [k for k,v in counts.items() if v > 1]
