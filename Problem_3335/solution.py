class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counts = [0] * 26
        for c in s:
            counts[ord(c)-ord('a')] += 1
        
        for i in range(t):
            z = counts[-1]
            counts = [counts[-1]] + counts[:-1]
            counts[1] += z
        return sum(counts) % (10**9+7)

