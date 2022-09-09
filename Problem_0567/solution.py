from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        n = len(s1)
        s1 = Counter(s1)
        perm = Counter(s2[:n])
        if perm == s1:
            return True
        
        for i in range(len(s2)-n):
            perm[s2[i]] -= 1
            perm[s2[i+n]] += 1
            if perm == s1:
                return True
        
        return False
